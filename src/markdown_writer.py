from datetime import datetime
from pathlib import Path


def format_list(items: list[str]) -> str:
    if not items:
        return "- 없음"

    return "\n".join(f"- {item}" for item in items)


def format_tags(tags: list[str]) -> str:
    if not tags:
        return "[]"

    return "[" + ", ".join(tags) + "]"


def save_markdown(
    note: dict,
    output_dir: str | Path = "output",
) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M")
    file_date = now.strftime("%Y-%m-%d_%H-%M-%S")

    file_name = f"{file_date}-note.md"
    file_path = output_path / file_name

    markdown_lines = [
        "---",
        f"created: {created_at}",
        f"tags: {format_tags(note['tags'])}",
        "---",
        "",
        f"# {note['title']}",
        "",
        "## Summary",
        "",
        note["summary"],
        "",
        "## Companies",
        "",
        format_list(note["companies"]),
        "",
        "## Sectors",
        "",
        format_list(note["sectors"]),
        "",
        "## Original Text",
        "",
        note["original_text"],
        "",
        "## My Thoughts",
        "",
        note["my_thoughts"] or "아직 작성된 생각이 없습니다.",
        "",
    ]

    markdown = "\n".join(markdown_lines)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(markdown)

    return file_path