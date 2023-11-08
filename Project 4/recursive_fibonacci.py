def nth_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


if __name__ == "__main__":
    print("This program computes the nth term of the Fibonacci sequence.")
    n = int(input("Enter an integer for n: "))
    if n < 0:
        print("n must be nonnegative.")
    elif n % 10 == 1:
        print(f"The {n}st term of the Fibonacci sequence is {nth_fibonacci(n)}.")
    elif n % 10 == 2:
        print(f"The {n}nd term of the Fibonacci sequence is {nth_fibonacci(n)}.")
    elif n % 10 == 3:
        print(f"The {n}rd term of the Fibonacci sequence is {nth_fibonacci(n)}.")
    else:
        print(f"The {n}th term of the Fibonacci sequence is {nth_fibonacci(n)}.")
