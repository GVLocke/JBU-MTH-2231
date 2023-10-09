def baseconversion(number, base):
    """Converts a number from base 10 to another base"""
    quotient = number
    result = []
    while quotient > 0:
        remainder = quotient % base
        quotient = quotient // base
        if remainder >= 10:
            result.append(chr(ord("A") + remainder - 10))
        else:
            result.append(remainder)
    return "".join([str(i) for i in reversed(result)])


number = int(input("Enter an integer: "))
base = int(input("Enter a base: "))
print(baseconversion(number, base))
