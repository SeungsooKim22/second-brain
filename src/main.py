from pathlib import Path

from input_handler import load_text
from markdown_writer import save_markdown
from processor import process_text

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "examples" / "sample_input.txt"
OUTPUT_DIR = BASE_DIR / "output"

def main() -> None:
    text = load_text(INPUT_PATH)
    note = process_text(text)
    saved_path = save_markdown(note, OUTPUT_DIR)
    
    print(f"Markdown file saved: {saved_path}")

if __name__ == "__main__":
    main()