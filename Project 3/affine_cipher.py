# the gcd function that I wrote for problem 6
from gcd import gcd
from bezout_coefficients import extended_gcd


class InvalidParameterError(Exception):
    pass


def convert_string_to_numbers(string):
    string = "".join(char for char in string if char.isalpha())
    return "".join([str(ord(char) - ord("a")).zfill(2) for char in string])
    # the first bit removes anything other than letters
    # concatenates together all the strings in a list of strings constructed by the following list comprehension:
    # for each character in the string
    # takes the ASCII value of each character and subtracts the ASCII value of 'a'.
    # pads the digits with zeros until the string is two digits.


def convert_numbers_to_string(number_string):
    return "".join(
        [
            chr(int(number_string[i : i + 2]) + ord("a"))
            for i in range(0, len(number_string), 2)
        ]
    )


def encrypt(string, a, b):
    if b >= 26:
        raise InvalidParameterError("Parameter b must be less than 26")
    if gcd(a, 26) != 1:
        raise InvalidParameterError("Parameter a must be relatively prime with 26")
    string = string.lower()
    string = convert_string_to_numbers(string)
    encrypted_string = ""
    for i in range(0, len(string), 2):
        pair_integer = (int(string[i : i + 2]) * a + b) % 26
        encrypted_string += str(pair_integer).zfill(2)
    return convert_numbers_to_string(encrypted_string)


def decrypt(encrypted_string, a, b):
    if b >= 26:
        raise InvalidParameterError("Parameter b must be less than 26")
    if gcd(a, 26) != 1:
        raise InvalidParameterError("Parameter a must be relatively prime with 26")
    inverse_a = extended_gcd(26, a)[2] % 26
    decrypted_string = ""
    for char in encrypted_string:
        char_integer = int(convert_string_to_numbers(char))
        char_integer = (char_integer - b) % 26
        char_integer = (char_integer * inverse_a) % 26
        decrypted_string += str(char_integer).zfill(2)
    return convert_numbers_to_string(decrypted_string)


if __name__ == "__main__":
    mystring = input("Enter a string of text: ")
    a = int(input("Enter an integer relatively prime with 26: "))
    b = int(input("Enter a number less than 26: "))
    print(f"Here it is encrypted: {encrypt(mystring, a, b)}")
    print(
        f"Here it is decrypted again (Trust me I used an algorithm): {decrypt(encrypt(mystring, a, b), a, b)}"
    )
