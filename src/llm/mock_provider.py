from .base import BaseLLM

class MockLLM(BaseLLM):
    def analyze(self, text: str) -> dict:
        
        return {
            "title": "AbCellera",
            "summary": "Mock AI가 생성한 요약입니다.",
            "companies": ["AbCellera"],
            "sectors": ["Biotechnology"],
            "tags": ["AI", "Biotech", "Investment"],
        }