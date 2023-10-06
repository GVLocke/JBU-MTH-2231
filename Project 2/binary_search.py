class Solution(object):
    def binary_search(self, list, target):
        """Takes an ordered list of n integers and determines the position of an integer using a binary search.
        returns -1 if the target is not found."""
        for i, x in enumerate(list):
            if x == target:
                return i
        return -1


# test code
test = Solution()
mylist = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = test.binary_search(mylist, 55)
if result == -1:
    print("Target not found.")
else:
    print(result)
