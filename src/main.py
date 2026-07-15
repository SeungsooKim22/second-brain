from pathlib import Path

from folder_manager import get_vault_path, navigate_folders
from input_handler import load_text
from markdown_writer import save_markdown
from processor import process_text
from storage_history import record_storage_event
from storage_recommender import recommend_storage_folder


BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "examples" / "sample_input.txt"


def main() -> None:
    text = load_text(INPUT_PATH)
    note = process_text(text)

    vault_path = get_vault_path()
    recommended_folder = recommend_storage_folder(note)

    selected_folder = None

    if recommended_folder is not None:
        print("\n과거 저장 이력을 기반으로 위치를 추천합니다.")
        print(f"추천 위치: {recommended_folder}")

        answer = input(
            "이 위치에 저장할까요? (y/n): "
        ).strip().lower()

        if answer in {"y", "yes", "예", "ㅇ"}:
            selected_folder = recommended_folder

    if selected_folder is None:
        selected_folder = navigate_folders(vault_path)

    if selected_folder is None:
        print("저장을 취소했습니다.")
        return

    saved_path = save_markdown(note, selected_folder)

    record_storage_event(
        note=note,
        selected_folder=selected_folder,
        saved_file=saved_path,
    )

    print(f"Obsidian note saved: {saved_path}")
    print("Storage history updated.")


if __name__ == "__main__":
    main()