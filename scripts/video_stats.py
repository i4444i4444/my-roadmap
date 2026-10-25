
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VIDEOS_FILE = REPO_ROOT / "videos.md"
STATS_FILE = REPO_ROOT / "VIDEO_STATS.md"

VIDEO_REGEX = re.compile(r"^\s*-\s+\[([ xX])\]\s+")


def create_progress_bar(completed, total, width=20):
    if total == 0:
        return "░" * width

    filled = round(completed / total * width)
    return "█" * filled + "░" * (width - filled)


def read_video_stats():
    if not VIDEOS_FILE.exists():
        raise FileNotFoundError(
            f"Could not find videos.md: {VIDEOS_FILE}"
        )

    content = VIDEOS_FILE.read_text(encoding="utf-8")

    sections = []
    current_section = None

    for line in content.splitlines():
        heading = re.match(r"^##\s+(.+?)\s*$", line)

        if heading:
            current_section = {
                "name": heading.group(1),
                "completed": 0,
                "total": 0,
            }
            sections.append(current_section)
            continue

        match = VIDEO_REGEX.match(line)

        if match and current_section is not None:
            current_section["total"] += 1

            if match.group(1).lower() == "x":
                current_section["completed"] += 1

    return sections


def generate_report(sections):
    total_videos = sum(section["total"] for section in sections)
    completed_videos = sum(
        section["completed"] for section in sections
    )
    remaining_videos = total_videos - completed_videos

    percentage = (
        completed_videos / total_videos * 100
        if total_videos
        else 0
    )

    lines = [
        "# Video Learning Progress",
        "",
        "Automatically generated from [videos.md](videos.md).",
        "",
        "## Overall Progress",
        "",
        f"- **Completed:** {completed_videos} / {total_videos}",
        f"- **Remaining:** {remaining_videos}",
        f"- **Progress:** {percentage:.1f}%",
        "",
        f"`{create_progress_bar(completed_videos, total_videos)}`",
        "",
        "## Progress by Topic",
        "",
        "| Topic | Completed | Remaining | Progress |",
        "|---|---:|---:|---:|",
    ]

    for section in sections:
        completed = section["completed"]
        total = section["total"]
        remaining = total - completed
        section_percentage = (
            completed / total * 100 if total else 0
        )
        bar = create_progress_bar(completed, total)

        lines.append(
            f"| {section['name']} "
            f"| {completed}/{total} "
            f"| {remaining} "
            f"| {section_percentage:.1f}% `{bar}` |"
        )

    lines.extend([
        "",
        "---",
        "",
        "*This file is generated automatically. "
        "Edit `videos.md` to update your progress.*",
        "",
    ])

    return "\n".join(lines)


def main():
    sections = read_video_stats()
    report = generate_report(sections)

    STATS_FILE.write_text(report, encoding="utf-8")

    total = sum(section["total"] for section in sections)
    completed = sum(
        section["completed"] for section in sections
    )

    print("Video statistics updated successfully.")
    print(f"Completed: {completed}/{total}")
    print(f"Report saved to: {STATS_FILE}")


if __name__ == "__main__":
    main()