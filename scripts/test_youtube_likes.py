import io
import json
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from xml.etree import ElementTree

from update_youtube_likes import badge, fetch_statistics


class YoutubeTests(unittest.TestCase):
    def test_batches_and_missing_counts(self):
        responses = [io.BytesIO(json.dumps({'items': [
            {'id': 'video0', 'statistics': {'likeCount': '0'}},
            {'id': 'video1', 'statistics': {}},
        ]}).encode()), io.BytesIO(b'{"items": []}')]
        with patch('update_youtube_likes.urlopen', side_effect=responses) as mock:
            self.assertEqual(fetch_statistics([f'video{i}' for i in range(51)], 'secret'), {'video0': 0})
            self.assertEqual(mock.call_count, 2)
            self.assertNotIn('secret', mock.call_args.args[0].full_url)

    def test_error_does_not_expose_key(self):
        error = HTTPError('https://example.test/?key=secret', 403, 'secret', {}, None)
        with patch('update_youtube_likes.urlopen', side_effect=error):
            with self.assertRaises(RuntimeError) as caught:
                fetch_statistics(['video'], 'secret')
            self.assertNotIn('secret', str(caught.exception))

    def test_badges_are_valid_and_zero_is_not_missing(self):
        for entry, expected in [(None, 'Watch'), ({'likes': 0, 'updated_at': 'today'}, '0 likes'),
                                ({'likes': 12345, 'updated_at': 'today'}, '12,345 likes')]:
            svg = badge(entry)
            ElementTree.fromstring(svg)
            self.assertIn(expected, svg)


if __name__ == '__main__':
    unittest.main()
