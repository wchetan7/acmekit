def charge(amount_cents: int, currency: str = "USD") -> dict:
    """Create a charge and return a receipt dictionary."""
    if amount_cents <= 0:
        raise ValueError("amount_cents must be positive")
    return {"amount_cents": amount_cents, "currency": currency, "status": "paid"}
