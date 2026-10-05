def charge(amount_cents: int, currency: str = "USD") -> dict:
    """Create a charge and return a receipt dictionary."""
    if amount_cents <= 0:
        raise ValueError("amount_cents must be positive")
    return {"amount_cents": amount_cents, "currency": currency, "status": "paid"}


def refund(receipt: dict, amount_cents: int | None = None) -> dict:
    """Refund all or part of a receipt."""
    paid = receipt["amount_cents"]
    if amount_cents is None:
        amount_cents = paid
    if amount_cents <= 0 or amount_cents > paid:
        raise ValueError("invalid refund amount")
    return {
        "amount_cents": amount_cents,
        "currency": receipt["currency"],
        "status": "refunded",
    }
