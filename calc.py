def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)


def get_discount(price, is_member):
    if is_member:
        return price * 0.9
    return price