class InvalidAIBackendError(Exception):
    def __init__(self, alias):
        super().__init__(f"Invalid AI backend: {alias}")


class InvalidBackendConfigurationError(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid backend configuration: {message}")
