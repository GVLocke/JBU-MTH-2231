from gcd import gcd
from td_prime_factorization import trial_division
from affine_cipher import convert_string_to_numbers


class InvalidParameterError(Exception):
    pass


def rsa_encrypt(message, p, q, e):
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
    message = convert_string_to_numbers(message)
    blocksize_string = "25"
    while int(blocksize_string) <= (p * q):
        blocksize_string += "25"
    blocksize_string = blocksize_string[:-2]
    blocksize = len(blocksize_string)
    message_blocks = [
        message[i : i + blocksize] for i in range(0, len(message), blocksize)
    ]
    encrypted_message = []
    for block in message_blocks:
        blockstring = str((int(block) ** e) % (p * q))
        while len(blockstring) % blocksize != 0:
            blockstring += "_"
        encrypted_message.append(blockstring)
    return encrypted_message


if __name__ == "__main__":
    message_string = input("Enter the message string: ")
    p = int(input("Enter the value for p: "))
    q = int(input("Enter the value for q: "))
    e = int(input("Enter the value for e: "))

    outputstring = ""
    for block in rsa_encrypt(message_string, p, q, e):
        print(block, end=" ")
