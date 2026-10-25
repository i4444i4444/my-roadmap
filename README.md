# My Roadmap

A personal learning roadmap and knowledge base for tracking progress, organizing study materials, and building reusable programming resources.

## Contents

| File | Description |
|---|---|
| [roadmap.md](roadmap.md) | Main learning roadmap and study progress |
| [algorithms.md](algorithms.md) | Notes on algorithms and learning materials |
| [snippets.md](snippets.md) | Reusable algorithms and code snippets |
| [videos.md](videos.md) | Video resources and learning checklist |
| [video_stats.md](video_stats.md) | Video watching statistics and progress |


## Learning Progress

### Roadmap

Use checkboxes in [roadmap.md](roadmap.md) to track completed learning tasks.

### Videos

The [videos.md](videos.md) file contains learning resources organized by topic. Mark a video as watched by changing `- [ ]` to `- [x]`.

The [video statistics report](video_stats.md) summarizes completed videos, remaining videos, and progress by topic.

## Automation

Scripts in the [`scripts/`](scripts/) directory automate routine tasks.

- [`video_stats.py`](scripts/video_stats.py) — calculates video completion statistics and generates `VIDEO_STATS.md`.
- [`fetch_video_titles.py`](scripts/fetch_video_titles.py) — retrieves YouTube video titles and channel names for supported entries in `videos.md`.
- [`stats.py`](scripts/stats.py) — generates learning roadmap progress statistics.

## Knowledge Management

Study notes and resources are organized into Markdown files. The repository keeps learning materials, progress tracking, and reusable code in one place.

## Workflow

1. Add learning resources to the relevant Markdown file.
2. Mark completed tasks and watched videos using checkboxes.
3. Run the appropriate Python script to regenerate statistics.
4. Commit and push changes to keep the repository up to date.
