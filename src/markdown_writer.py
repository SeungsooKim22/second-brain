from pathlib import Path
from datetime import datetime

def save_markdown(content, output_dir="output"):
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    file_name = f"{today}-note.md"
    file_path = output_path / file_name

    markdown = f"""# Second Brain Note


Date: {today}

## Original Text
{content}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    return file_path