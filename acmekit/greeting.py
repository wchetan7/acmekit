def greet(name: str, formal: bool = False) -> str:
    """Return a greeting for the given name."""
    if formal:
        return f"Good day, {name}."
    return f"Hi {name}!"



def greet_all(names: list[str], formal: bool = False) -> list[str]:
    """Return a greeting for each name."""
    return [greet(name, formal) for name in names]
