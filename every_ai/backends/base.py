from typing import List, Optional, Generic, Protocol, TypeVar, runtime_checkable, Type

ConfigClass = TypeVar("ConfigClass", covariant=True)


@runtime_checkable
class ChatAbility(Protocol):
    def chat(
        self, *, system_messages: Optional[List[str]] = None, user_messages: List[str]
    ) -> str:
        ...


@runtime_checkable
class EmbeddingAbility(Protocol):
    def embed(self, inputs: List[str]) -> List[List[float]]:
        ...

    @property
    def embedding_output_dimensions(self) -> int:
        ...


class AIBackend(Generic[ConfigClass]):
    def __init__(self, config: ConfigClass):
        ...
