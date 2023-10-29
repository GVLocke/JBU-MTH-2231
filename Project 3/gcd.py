def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)


if __name__ == "__main__":
    bigger_integer = int(input("Enter an integer: "))
    smaller_integer = int(input("Enter another integer: "))
    # if bigger_integer < smaller_integer:
    #     temp = smaller_integer
    #     smaller_integer = bigger_integer
    #     bigger_integer = temp
    print(gcd(bigger_integer, smaller_integer))
