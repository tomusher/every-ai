from .base import AIBackend, ChatAbility, EmbeddingAbility  # noqa: F401
from .registry import _registry as registry  # noqa: F401


def prepare():
    from . import (
        anthropic,  # noqa: F401
    )
