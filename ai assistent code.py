def is_happy(n):
    """Check if a number is a happy number."""
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


def find_happy_numbers(limit):
    """Find all happy numbers up to a given limit."""
    happy_nums = []
    for num in range(1, limit + 1):
        if is_happy(num):
            happy_nums.append(num)
    return happy_nums


if __name__ == "__main__":
    limit = 100
    happy_numbers = find_happy_numbers(limit)
    print(f"Happy numbers up to {limit}: {happy_numbers}")
