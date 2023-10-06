def firstAndLastLargest(self, list):
    """Takes a list of n integers and determines the first and last occurence of the largest element in the list."""
    max_value = max(list)
    occurrences = [i for i, x in enumerate(list) if x == max_value]
    return [min(occurrences), max(occurrences)]


# test code
mylist = [1, 2, 3, 4, 3, 4, 1, 4]
print(firstAndLastLargest(mylist))
