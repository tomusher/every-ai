from typing import List

from every_ai import AIBackend


class MockAllFeaturesBackend(AIBackend):
    def __init__(self, config):
        pass

    def chat(self, prompt: str) -> str:
        return "AI! Don't talk to me about AI!"

    def embed(self, inputs: List[str]) -> List[List[float]]:
        return [[0.1, 0.2, 0.3] for _ in range(len(inputs))]


class MockChatOnlyBackend(AIBackend):
    def chat(self, prompt: str) -> str:
        return "AI! Don't talk to me about AI!"


class MockEmbedOnlyBackend(AIBackend):
    def embed(self, inputs: List[str]) -> List[List[float]]:
        return [[0.1, 0.2, 0.3] for _ in range(len(inputs))]

    @property
    def embedding_output_dimensions(self) -> int:
        return 3
