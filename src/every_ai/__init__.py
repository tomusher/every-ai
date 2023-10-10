import importlib
import pkgutil

import every_ai.backends

from .base import AIBackend, ChatAbility, EmbeddingAbility  # noqa: F401
from .exceptions import InvalidAIBackendError
from .registry import _registry as registry


def discover():
    """Discover all the backends in the backends directory"""

    for _, name, _ in pkgutil.iter_modules(every_ai.backends.__path__):
        importlib.import_module(f"every_ai.backends.{name}")


def init(backend_name: str, **config) -> AIBackend:
    """Initialise a backend with the given name and config"""
    discover()

    try:
        backend_cls = registry._registry[backend_name]
    except KeyError as e:
        raise InvalidAIBackendError(backend_name) from e
    return backend_cls(config)
