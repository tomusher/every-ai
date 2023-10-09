from typing import TYPE_CHECKING

from .backends import registry
from .backends.exceptions import InvalidAIBackendError
from .backends.base import BackendProtocol

VERSION = (1, 0, 0)
__version__ = ".".join(map(str, VERSION))


def init(backend_name: str, **config) -> BackendProtocol:
    """Initialise a backend with the given name and config"""
    try:
        backend_cls = registry._registry[backend_name]
    except KeyError as e:
        raise InvalidAIBackendError(backend_name) from e
    return backend_cls(config)
