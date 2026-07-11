from llm.factory import create_llm

def process_text(text: str) ->dict:
    llm = create_llm()
    analysis = llm.analyze(text)
    
    return {
        "title": analysis.get("title", "Second Brain Note"),
        "summary": analysis.get("summary", "AI 요약 기능이 아직 연결되지 않았습니다."),
        "companies": analysis.get("companies", []),
        "sectors": analysis.get("sectors", []),
        "tags": analysis.get("tags", []),
        "original_text": text,
        "my_thoughts": "",
    }