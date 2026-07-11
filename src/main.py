import os

from pathlib import Path

from dotenv import load_dotenv

from input_handler import load_text
from markdown_writer import save_markdown
from processor import process_text

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "examples" / "sample_input.txt"


def main() -> None:
    load_dotenv(BASE_DIR / ".env")

    vault_path = os.getenv("OBSIDIAN_VAULT_PATH")

    if not vault_path:
        raise ValueError(
            "OBSIDIAN_VAULT_PATH가 설정되지 않았습니다."
            " .env 파일을 확인하세요.")
    
    output_dir = Path(vault_path) / "00 Inbox"
    output_dir.mkdir(parents=True, exist_ok=True)

    text = load_text(INPUT_PATH)
    note = process_text(text)
    saved_path = save_markdown(note, output_dir)
    
    print(f"Obsidian note saved: {saved_path}")

if __name__ == "__main__":
    main()