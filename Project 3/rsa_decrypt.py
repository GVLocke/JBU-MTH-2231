from gcd import gcd
from td_prime_factorization import trial_division
from bezout_coefficients import extended_gcd
from affine_cipher import convert_numbers_to_string


class InvalidParameterError(Exception):
    pass


def rsa_decrypt(message, p, q, e):
    if len(trial_division(p)) != 1 or p % 2 == 0:
        raise InvalidParameterError("Parameter P must be an odd prime")
    if len(trial_division(q)) != 1 or p % 2 == 0:
        raise InvalidParameterError("Parameter Q must be an odd prime")
    if e <= 1:
        raise InvalidParameterError("Parameter E must be greater than 1")
    if gcd(e, (p - 1) * (q - 1)) != 1:
        raise InvalidParameterError(
            "Parameter E must be relatively prime to (p-1)*(q-1)"
        )
    d = extended_gcd((p - 1) * (q - 1), e)[2]
    decrypted_message = ""
    for block in message:
        block_integer = int("".join(char for char in block if char.isnumeric()))
        decrypted_message += str((block_integer**d) % (p * q)).zfill(len(message[0]))
    return convert_numbers_to_string(decrypted_message)


if __name__ == "__main__":
    encrypted_message = input(
        "Enter the encrypted message, with numbers separated by spaces: "
    ).split()
    p = int(input("Enter an odd prime number for p: "))
    q = int(input("Enter an odd prime number for q: "))
    e = int(input("Enter a number e such that gcd(e, (p-1)*(q-1)) = 1: "))
    print(rsa_decrypt(encrypted_message, p, q, e))
