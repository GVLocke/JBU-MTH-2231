def number7(x, y, a, b, k):
    n = 1
    if k == 0:
        b = a
    else:
        while n < k:
            temp = b
            b = x * b + y * a
            a = temp
            n += 1
    return b


print(
    "This program computes a recurrence relation (a_n = c1 * a_(n-1) + c2 * a_(n-2)) up to some k. All inputs should be integers."
)
coefficient1 = int(input("Enter the first coefficient (c1): "))
coefficient2 = int(input("Enter the second coefficient (c2): "))
condition1 = int(input("Enter the a_0 term: "))
condition2 = int(input("Enter the a_1 term: "))
k = int(input("Enter some k: "))
print(number7(coefficient1, coefficient2, condition1, condition2, k))
