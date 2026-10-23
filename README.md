# My Roadmap

A personal repository for tracking my development journey: study plan, notes, reusable code snippets, and graph-based knowledge notes.

## What's inside

| File / folder        | Purpose                                                        |
| -------------------- | -------------------------------------------------------------- |
| `roadmap.md`         | Main learning plan with checkboxes                             |
| `algorithms.md`      | Notes from the book                                            |
| `snippets.md`        | Common algorithms and code snippets (sorting, searching, etc.) |
| `videos.md`          | Videos and courses to watch                                    |
| `scripts/`           | Python scripts for automation                                  |
| `.github/workflows/` | GitHub Actions (auto-updating stats)                           |
| `STATS.md`           | Auto-generated progress bar (created by script)                |

## Note format

Notes are kept in [Obsidian](https://obsidian.md/) as a knowledge graph: topics are linked via `[[wiki-links]]`. The vault *is* this repository, so the graph and Git history live together.

## Automation

- `scripts/stats.py` — counts completed tasks in `roadmap.md` and generates `STATS.md` with a progress bar.
- GitHub Actions runs the script on every push to `main` and commits the updated `STATS.md`.