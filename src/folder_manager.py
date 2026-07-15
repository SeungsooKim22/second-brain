import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent


def get_vault_path() -> Path:
    """
    .env 파일에서 Obsidian Vault 경로를 불러온다.
    """
    load_dotenv(BASE_DIR / ".env")

    vault_path = os.getenv("OBSIDIAN_VAULT_PATH")

    if not vault_path:
        raise ValueError(
            "OBSIDIAN_VAULT_PATH가 설정되지 않았습니다. "
            ".env 파일을 확인하세요."
        )

    path = Path(vault_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Obsidian Vault를 찾을 수 없습니다: {path}"
        )

    return path


def get_subfolders(parent_path: Path) -> list[Path]:
    """
    지정한 폴더 바로 아래에 있는 하위 폴더를 가져온다.

    .obsidian처럼 이름이 점(.)으로 시작하는 내부 폴더는 제외한다.
    """
    folders = [
        path
        for path in parent_path.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    ]

    return sorted(
        folders,
        key=lambda path: path.name.lower(),
    )


def display_folder_menu(
    current_path: Path,
    vault_path: Path,
) -> list[Path]:
    """
    현재 위치의 하위 폴더를 번호와 함께 출력한다.
    """
    folders = get_subfolders(current_path)

    try:
        relative_path = current_path.relative_to(vault_path)
        if str(relative_path) == ".":
            location = vault_path.name
        else:
            location = (
                vault_path.name
                + " / "
                + " / ".join(relative_path.parts)
            )
    except ValueError:
        location = str(current_path)

    print("\n" + "=" * 50)
    print(f"현재 위치: {location}")
    print("=" * 50)

    print("0. 새로운 폴더 추가")

    for index, folder in enumerate(folders, start=1):
        print(f"{index}. {folder.name}")

    if current_path != vault_path:
        print("9. 이전 폴더")

    print("s. 현재 위치 선택")
    print("q. 종료")

    return folders


def create_folder(parent_path: Path) -> Path | None:
    """
    현재 위치에 새로운 하위 폴더를 생성한다.
    """
    folder_name = input(
        "새 폴더 이름을 입력하세요. "
        "(취소하려면 Enter): "
    ).strip()

    if not folder_name:
        print("폴더 생성을 취소했습니다.")
        return None

    new_folder = parent_path / folder_name

    if new_folder.exists():
        print(f"이미 존재하는 폴더입니다: {folder_name}")
        return None

    new_folder.mkdir(parents=True, exist_ok=False)

    print(f"폴더를 생성했습니다: {new_folder}")

    return new_folder


def navigate_folders(vault_path: Path) -> Path | None:
    """
    사용자가 폴더를 탐색하고 최종 저장 위치를 선택하게 한다.
    """
    current_path = vault_path

    while True:
        folders = display_folder_menu(
            current_path=current_path,
            vault_path=vault_path,
        )

        choice = input("\n선택: ").strip().lower()

        if choice == "q":
            print("폴더 선택을 종료했습니다.")
            return None

        if choice == "s":
            print(f"선택한 저장 위치: {current_path}")
            return current_path

        if choice == "0":
            new_folder = create_folder(current_path)

            if new_folder is not None:
                current_path = new_folder

            continue

        if choice == "9" and current_path != vault_path:
            current_path = current_path.parent
            continue

        if not choice.isdigit():
            print("번호, s 또는 q를 입력해주세요.")
            continue

        folder_index = int(choice) - 1

        if folder_index < 0 or folder_index >= len(folders):
            print("목록에 있는 올바른 번호를 선택해주세요.")
            continue

        current_path = folders[folder_index]


if __name__ == "__main__":
    vault = get_vault_path()
    selected_folder = navigate_folders(vault)

    if selected_folder is not None:
        print(f"\n최종 선택 경로: {selected_folder}")