from pathlib import Path
from input_handler import load_text
from markdown_writer import save_markdown

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "examples" / "sample_input.txt"

text = load_text(file_path)
saved_path = save_markdown(text, BASE_DIR / "output")


print(f"Markdown file saved: {saved_path}")