def bit_string(n, string=""):
    if n == 0:
        print(string)
    else:
        bit_string(n - 1, string + "1")
        if not string or string[-1] == "1":
            bit_string(n - 1, string + "0")


n = int(input("Enter the value of n: "))
bit_string(n)
