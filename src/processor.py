def process_text(text: str) ->dict:
    """
    입력된 원문을 Second Brain 노트 형식에 맞는 데이터로 변환한다.

    현재는 AI를 사용하지 않기 때문에 원문과 기본값만 반환한다.
    이후 함수에 LLM 요약과 태그 추출 기능을 추가한다.
    """
    return {
        "title": "Second Brain Note",
        "summary": "AI 요약 기능이 아직 연결되지 않았습니다.",
        "companies": [],
        "sectors": [],
        "tags": [],
        "original_text": text,
        "my_thoughts": "",
    }