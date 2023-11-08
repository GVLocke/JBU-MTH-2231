def aTo2ToN(a, n):
    return a * a if n == 1 else (a * a) * aTo2ToN(a, n - 1)


if __name__ == "__main__":
    print("This program computes a^2^n")
    a = float(input("Enter a real number for a: "))
    n = int(input("Enter a nonnegative integer for n: "))
    print(aTo2ToN(a, n))
