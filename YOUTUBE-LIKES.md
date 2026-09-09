# 音乐页面自动更新点赞数

## 首次启用

1. 在 Google Cloud 控制台创建或选择项目，启用 **YouTube Data API v3**，创建 API key。建议将 API 限制为 YouTube Data API v3。此密钥由 GitHub Actions 服务端使用，不要设置为浏览器 HTTP referrer 限制。
2. 在 GitHub 仓库 Settings → Secrets and variables → Actions → New repository secret 中添加 `YOUTUBE_API_KEY`。不要把密钥提交到源码或发到聊天里。
3. 提交并推送本次修改到 `master`。
4. 在 Settings → Pages → Build and deployment → Source 中选择 **GitHub Actions**。
5. 在 Actions 中选择 **Update music likes and deploy Pages** → Run workflow。

工作流同时负责网站发布：master 更新、手动运行以及每天 UTC 05:23 都会触发。定时运行可能延迟；公开仓库长期无活动时 GitHub 可能停用定时任务，需要重新启用。

## 原理

脚本从 `_includes/music/list.md` 的 YouTube 链接提取视频 ID，每批最多 50 个，通过官方 API 获取点赞数，然后生成 `img/youtube-likes/*.svg`。Jekyll 构建完成后直接发布 Pages，不需要个人 GitHub token，也不依赖机器人提交再次触发 Pages。

成功获取的数值保存在 Actions cache。API 请求失败时保留缓存数据并继续发布网站，但工作流会标红提醒。缓存可能被 GitHub 清理；没有缓存或视频不可用/不公开点赞数时，显示 Watch，不伪造数字。鼠标悬停在有数字的徽章上可查看数据更新时间。

仓库自带的 SVG 初始显示 Watch；真实数字在配置密钥并成功运行工作流后出现在已发布网站中。运行时数据和更新后的 SVG 不回写 Git 仓库。

## 添加歌曲

保持原有表格结构，徽章路径使用下面格式（两处替换为同一个视频 ID）：

```markdown
[![YouTube Video Likes]({{ site.baseurl }}/img/youtube-likes/VIDEO_ID.svg)](https://www.youtube.com/watch?v=VIDEO_ID)
```

## 本地验证

```sh
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/update_youtube_likes.py --render-only
```

本地获取真实数值需通过环境变量设置 `YOUTUBE_API_KEY`，然后运行 `python scripts/update_youtube_likes.py`。
