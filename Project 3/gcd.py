def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)


if __name__ == "__main__":
    m = int(input("Enter an integer: "))
    n = int(input("Enter another integer: "))
    print(gcd(m, n))
