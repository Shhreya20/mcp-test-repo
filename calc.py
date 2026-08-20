def calculate_average(numbers):
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
