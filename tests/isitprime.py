import math


def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(2, limit + 1) if primes[i]]


def isPrime(number):
    primes = sieve_of_eratosthenes(int(math.sqrt(number)))
    for i in primes:
        if number % i == 0:
            return False
    return True


mynum = int(input("Enter an integer: "))
print(isPrime(mynum))
