# Payments

`charge(amount_cents, currency="USD")` creates a charge and returns a receipt.

- The amount is in cents and must be positive.
- The receipt contains `amount_cents`, `currency` and `status` (`"paid"`).
