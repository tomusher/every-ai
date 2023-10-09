import pytest

import every_ai
from every_ai.backends import registry

from mock_backend import MockBackend


def test_registering_mock_backend():
    registry.register("mock")(MockBackend)
    assert "mock" in registry._registry.keys()
    assert registry._registry["mock"] == MockBackend


def test_init_backend():
    registry.register("mock")(MockBackend)
    backend = every_ai.init("mock", foo="bar")
    assert isinstance(backend, MockBackend)
