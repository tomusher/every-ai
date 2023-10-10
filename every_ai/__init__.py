from .backends import registry
from .backends.anthropic import AnthropicBackend  # noqa: F401
from .backends.base import AIBackend
from .backends.exceptions import InvalidAIBackendError
from .backends.openai import OpenAIBackend  # noqa: F401

VERSION = (1, 0, 0)
__version__ = ".".join(map(str, VERSION))


def init(backend_name: str, **config) -> AIBackend:
    """Initialise a backend with the given name and config"""
    try:
        backend_cls = registry._registry[backend_name]
    except KeyError as e:
        raise InvalidAIBackendError(backend_name) from e
    return backend_cls(config)
