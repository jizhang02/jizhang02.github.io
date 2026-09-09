"""Fetch public YouTube statistics and render local SVG badges (stdlib only)."""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def video_ids(root):
    text = (root / '_includes/music/list.md').read_text(encoding='utf-8')
    return sorted(set(re.findall(r'youtube\.com/watch\?v=([\w-]{11})(?![\w-])', text)))


def fetch_statistics(ids, key):
    result = {}
    for start in range(0, len(ids), 50):
        query = urlencode({'part': 'statistics', 'id': ','.join(ids[start:start + 50])})
        request = Request('https://www.googleapis.com/youtube/v3/videos?' + query,
                          headers={'X-Goog-Api-Key': key})
        try:
            with urlopen(request, timeout=30) as response:
                payload = json.load(response)
        except HTTPError as exc:
            raise RuntimeError(f'YouTube API returned HTTP {exc.code}; check API activation, key restrictions and quota.') from None
        except (URLError, TimeoutError, ValueError):
            raise RuntimeError('Could not read YouTube API response; previous data is unchanged.') from None
        if not isinstance(payload, dict) or not isinstance(payload.get('items'), list):
            raise RuntimeError('Unexpected API response; previous data is unchanged.')
        for item in payload['items']:
            count = item.get('statistics', {}).get('likeCount')
            if count is not None:
                count = str(count)
                if not re.fullmatch(r'[0-9]+', count):
                    raise RuntimeError('Invalid like count; previous data is unchanged.')
                result[item['id']] = int(count)
    return result


def badge(entry):
    if entry and entry.get('likes') is not None:
        message = format(entry['likes'], ',') + ' likes'
        title = 'YouTube: ' + message + '; updated ' + entry['updated_at']
    else:
        message, title = 'Watch', 'Watch on YouTube; like count unavailable'
    right = max(54, len(message) * 7 + 16)
    width = 70 + right
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20" role="img" aria-label="{escape(title, quote=True)}">'
            f'<title>{escape(title)}</title><rect width="{width}" height="20" rx="3" fill="#eee"/>'
            '<path d="M3 0h67v20H3a3 3 0 0 1-3-3V3a3 3 0 0 1 3-3" fill="#c00"/>'
            '<g font-family="Verdana,Arial,sans-serif" font-size="11" text-anchor="middle">'
            '<text x="35" y="14" fill="white">YouTube</text>'
            f'<text x="{70 + right / 2}" y="14" fill="#222">{escape(message)}</text></g></svg>\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--render-only', action='store_true')
    args = parser.parse_args()
    root = args.root
    ids = video_ids(root)
    if not ids:
        raise RuntimeError('No YouTube video IDs found in the music list.')
    data_path = root / '_data/youtube_likes.json'
    data = json.loads(data_path.read_text(encoding='utf-8')) if data_path.exists() else {}
    if not args.render_only:
        key = os.environ.get('YOUTUBE_API_KEY', '').strip()
        if not key:
            raise RuntimeError('Set the repository Actions secret YOUTUBE_API_KEY first.')
        counts = fetch_statistics(ids, key)
        now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
        # Omitted/private videos and hidden counts are unavailable, not zero.
        data = {video: {'likes': counts.get(video), 'updated_at': now} for video in ids}
        data_path.parent.mkdir(parents=True, exist_ok=True)
        temp = data_path.with_suffix('.tmp')
        temp.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        temp.replace(data_path)
        print(f'Updated {len(counts)} counts; {len(ids) - len(counts)} unavailable.')
    output = root / 'img/youtube-likes'
    output.mkdir(parents=True, exist_ok=True)
    for video in ids:
        (output / f'{video}.svg').write_text(badge(data.get(video)), encoding='utf-8')
    print(f'Rendered {len(ids)} badges.')


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, OSError, ValueError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(1)
