from pathlib import Path
from typing import Any

from storage_history import load_storage_history


def find_matching_history(
    note: dict[str, Any],
    history: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    현재 노트와 관련된 과거 저장 기록을 찾는다.

    첫 번째 버전에서는 같은 기업명이 포함된 기록을
    관련 기록으로 판단한다.
    """
    current_companies = {
        company.lower()
        for company in note.get("companies", [])
    }

    if not current_companies:
        return []

    matches = []

    for event in history:
        past_companies = {
            company.lower()
            for company in event.get("companies", [])
        }

        if current_companies & past_companies:
            matches.append(event)

    return matches


def recommend_storage_folder(note: dict[str, Any]) -> Path | None:
    """
    과거 저장 이력을 참고해 저장 폴더를 추천한다.

    같은 기업에 대한 기록이 여러 개라면
    가장 최근에 선택한 폴더를 추천한다.
    """
    history = load_storage_history()
    matching_history = find_matching_history(note, history)

    if not matching_history:
        return None

    latest_match = matching_history[-1]
    folder_path = Path(latest_match["selected_folder"])

    if not folder_path.exists():
        return None

    return folder_path