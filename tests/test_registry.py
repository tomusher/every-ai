import sys
from unittest.mock import MagicMock

import every_ai
from every_ai.backends import registry
from tests.mock_backends import MockAllFeaturesBackend


def test_registering_mock_backend():
    registry.register("mock")(MockAllFeaturesBackend)
    assert "mock" in registry._registry.keys()
    assert registry._registry["mock"] == MockAllFeaturesBackend


def test_init_backend():
    registry.register("mock")(MockAllFeaturesBackend)
    backend = every_ai.init("mock", foo="bar")
    assert isinstance(backend, MockAllFeaturesBackend)


def test_built_in_backends_exist():
    openai = MagicMock()
    sys.modules["openai"] = openai
    every_ai.init("openai", api_key="foo")
