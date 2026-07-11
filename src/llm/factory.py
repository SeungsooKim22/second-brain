from .mock_provider import MockLLM

def create_llm():
    return MockLLM()