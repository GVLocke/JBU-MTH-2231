def extended_gcd(dividend, divisor):
    if dividend == 0:
        return divisor, 0, 1
    else:
        gcd, bezout_divisor, bezout_dividend = extended_gcd(
            divisor % dividend, dividend
        )
        return (
            gcd,
            bezout_dividend - (divisor // dividend) * bezout_divisor,
            bezout_divisor,
        )


if __name__ == "__main__":
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    if a < b:
        temp = a
        a = b
        b = a
    gcd, x, y = extended_gcd(a, b)

    print(f"The gcd of {a} and {b} is {gcd}")
    print(f"The Bézout coefficients are {x} and {y}")
