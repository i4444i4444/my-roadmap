# My Roadmap

A personal repository for tracking my development journey: study plan, notes, reusable code snippets, videos, and graph-based knowledge notes.

## What's inside

| File / folder | Purpose |
|---|---|
| [roadmap.md](roadmap.md) | Main learning plan with checkboxes |
| [algorithms.md](algorithms.md) | Notes from the book |
| [snippets.md](snippets.md) | Common algorithms and code snippets |
| [videos.md](videos.md) | Videos and courses to watch |
| [scripts/](scripts/) | Python scripts for automation |
| [.github/workflows/](.github/workflows/) | GitHub Actions workflows |
| [STATS.md](STATS.md) | Automatically generated progress bar |

## Automation

- [`scripts/stats.py`](scripts/stats.py) — counts completed tasks in `roadmap.md` and generates `STATS.md` with a progress bar.
- GitHub Actions runs the statistics script on every push to `main` and commits the updated `STATS.md`.

## Note format

Notes are kept in [Obsidian](https://obsidian.md/) as a knowledge graph. Topics are connected via `[[wiki-links]]`. The repository serves as the vault, keeping the knowledge graph and Git history together.

## About

Personal learning roadmap and knowledge base covering study planning, algorithms, reusable code snippets, videos, and automated progress tracking.
