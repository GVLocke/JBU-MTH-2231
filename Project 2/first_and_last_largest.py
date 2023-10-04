# Given a list of n integerns, determine the first and last occurence of the largest element in the list.
class Solution(object):
    def firstAndLastLargest(self, list):
        max_value = max(list)
        occurrences = [i for i, x in enumerate(list) if x == max_value]
        return occurrences
    
# test code
bruh = Solution()
mylist = [1, 2, 3, 4, 3, 2, 1, 4]
print(bruh.firstAndLastLargest(mylist))