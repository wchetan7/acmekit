def greet(name: str, formal: bool = False) -> str:
    """Return a greeting for the given name."""
    if formal:
        return f"Good day, {name}."
    return f"Hi {name}!"
