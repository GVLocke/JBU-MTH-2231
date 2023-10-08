def baseconversion(number, base):
    """Converts a number from base 10 to another base"""
    quotient = number
    result = []
    while quotient > 0:
        remainder = quotient % base
        quotient = quotient // base
        result.append(remainder)
    return int("".join([str(i) for i in reversed(result)]))


print(baseconversion(12345, 8))
