def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)


def get_discount(price, is_member):
    if price < 0:
        raise ValueError("Price must be non-negative")
    if is_member:
        return price * 0.9
    return price


def calculate_tax(price):
    return price * 0.18


def apply_bulk_discount(prices, threshold, discount_rate):
    if not (0 <= discount_rate <= 1):
        raise ValueError("discount_rate must be between 0 and 1")
    total = sum(prices)
    if total > threshold:
        return total * (1 - discount_rate)
    return total