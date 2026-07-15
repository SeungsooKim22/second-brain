import json
from datetime import datetime
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
HISTORY_PATH = DATA_DIR / "storage_history.json"


def load_storage_history() -> list[dict[str, Any]]:
    """
    기존 저장 이력을 불러온다.

    이력 파일이 아직 없으면 빈 목록을 반환한다.
    """
    if not HISTORY_PATH.exists():
        return []

    with open(HISTORY_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_storage_history(
    history: list[dict[str, Any]],
) -> None:
    """
    저장 이력 전체를 JSON 파일에 저장한다.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(HISTORY_PATH, "w", encoding="utf-8") as file:
        json.dump(
            history,
            file,
            ensure_ascii=False,
            indent=2,
        )


def record_storage_event(
    note: dict,
    selected_folder: Path,
    saved_file: Path,
) -> None:
    """
    한 번의 저장 선택 결과를 저장 이력에 추가한다.
    """
    history = load_storage_history()

    event = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "title": note.get("title", ""),
        "summary": note.get("summary", ""),
        "companies": note.get("companies", []),
        "sectors": note.get("sectors", []),
        "tags": note.get("tags", []),
        "selected_folder": str(selected_folder),
        "saved_file": str(saved_file),
    }

    history.append(event)
    save_storage_history(history)