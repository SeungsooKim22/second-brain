def load_text(file_path):
    """
    텍스트 파일을 읽어서 문자열로 반환한다
    """
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text