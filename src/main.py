from pathlib import Path

from folder_manager import get_vault_path, navigate_folders
from input_handler import load_text
from markdown_writer import save_markdown
from processor import process_text


BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "examples" / "sample_input.txt"


def main() -> None:
    text = load_text(INPUT_PATH)
    note = process_text(text)

    vault_path = get_vault_path()
    selected_folder = navigate_folders(vault_path)

    if selected_folder is None:
        print("저장을 취소했습니다.")
        return

    saved_path = save_markdown(note, selected_folder)

    print(f"Obsidian note saved: {saved_path}")


if __name__ == "__main__":
    main()