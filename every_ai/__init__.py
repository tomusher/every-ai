from .backends import registry
from .backends.base import BackendProtocol
from .backends.exceptions import InvalidAIBackendError

VERSION = (1, 0, 0)
__version__ = ".".join(map(str, VERSION))


def init(backend_name: str, **config) -> BackendProtocol:
    """Initialise a backend with the given name and config"""
    try:
        backend_cls = registry._registry[backend_name]
    except KeyError as e:
        raise InvalidAIBackendError(backend_name) from e
    return backend_cls(config)
