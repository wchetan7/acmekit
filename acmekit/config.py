DEFAULTS = {"timeout_seconds": 30, "retries": 0}


def get(key: str):
    """Return a configuration value."""
    return DEFAULTS[key]
