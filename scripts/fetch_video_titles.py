import re
import json
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
VIDEOS_FILE = REPO_ROOT / "videos.md"

YOUTUBE_REGEX = re.compile(
    r'\[([^\]]*)\]\((https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[^\s\)]+)\)'
)

def get_metadata(url: str) -> dict | None:
    oembed_url = f"https://www.youtube.com/oembed?url={urllib.parse.quote(url)}&format=json"
    try:
        with urllib.request.urlopen(oembed_url, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def main():
    if not VIDEOS_FILE.exists():
        print(f"File {VIDEOS_FILE} not found.")
        return

    content = VIDEOS_FILE.read_text(encoding="utf-8")
    updated = False
    new_lines = []

    for line in content.splitlines():
        match = YOUTUBE_REGEX.search(line)
        if match and '- [' in line:
            old_text, url = match.groups()
            should_update = (
                not old_text.strip()
                or old_text.lower().startswith("video")
                or "youtube" in old_text.lower()
            )
            if not should_update:
                new_lines.append(line)
                continue

            print(f"Fetching: {url}")
            meta = get_metadata(url)
            if meta:
                title = meta.get("title", "Unknown")
                author = meta.get("author_name", "")
                prefix = line[:line.index('[')]
                new_line = f"{prefix}[{title}]({url}) — {author}"
                new_lines.append(new_line)
                updated = True
                print(f"   OK: {title} — {author}")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if updated:
        VIDEOS_FILE.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        print("\nvideos.md updated.")
    else:
        print("\nNothing to update.")

if __name__ == "__main__":
    main()