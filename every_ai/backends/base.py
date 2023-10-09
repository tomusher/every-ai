from typing import List, Optional, Protocol, TypeVar

ConfigClass = TypeVar("ConfigClass", covariant=True)


class ChatAbility(Protocol):
    def chat(
        self, *, system_messages: Optional[List[str]] = None, user_messages: List[str]
    ) -> str:
        ...


class EmbeddingAbility(Protocol):
    def embed(self, inputs: List[str]) -> List[List[float]]:
        ...

    @property
    def embedding_output_dimensions(self) -> int:
        ...


class BackendProtocol(Protocol[ConfigClass]):
    def __init__(self, config: ConfigClass):
        ...
