import random


def recursive_search(search_term, list, i=0):
    if list[i] == search_term:
        return i
    elif i == (len(list) - 1):
        return 0
    else:
        return recursive_search(search_term, list, i + 1)


if __name__ == "__main__":
    print(
        "This program checks if an element is in a list. The list is a randomly generated list of 10 integers from 1 to 20."
    )
    my_list = random.sample(range(1, 21), 10)
    search_term = int(input("Enter an integer to search for: "))
    result = recursive_search(search_term, my_list)
    if result == 0:
        print(f"{search_term} does not appear in the list.")
    else:
        print(f"{search_term} appears at index {result} in the list.")
    print(f"Here's what was in the list: {my_list}")
