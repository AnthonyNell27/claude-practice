def greet(names):
    """Return a list of "Hello, <name>!" strings for each name."""
    return [f"Hello, {name}!" for name in names]


def total_price(items):
    """Sum price * qty for each item (a dict with 'price' and 'qty' keys)."""
    return sum(item["price"] * item["qty"] for item in items)


def apply_discount(total, percent):
    """Return total reduced by percent percent (percent must be 0-100)."""
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return round(total - (total * percent / 100), 2)
