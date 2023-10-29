def trial_division(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > i:
        factors.append(n)

    return factors


if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    factors = trial_division(n)

    if factors == [n]:
        print(f"{n} is prime.")
    else:
        print(f"Factors of {n}: {factors}")
