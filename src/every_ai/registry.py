from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from .base import AIBackend


class BackendRegistry:
    """A registry to keep track of all the Backend classes that have been registered."""

    def __init__(self):
        self._registry: dict[str, Type["AIBackend"]] = {}

    def register(self, name):
        def decorator(cls: Type["AIBackend"]):
            self._registry[name] = cls
            return cls

        return decorator

    def __iter__(self):
        return iter(self._registry.items())


_registry = BackendRegistry()
