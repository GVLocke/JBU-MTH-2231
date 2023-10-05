class Solution(object):
    def firstAndLastLargest(self, list):
        """Takes a list of n integerns and determines the first and last occurence of the largest element in the list."""
        max_value = max(list)
        occurrences = [i for i, x in enumerate(list) if x == max_value]
        return occurrences
    
# test code
test = Solution()
mylist = [1, 2, 3, 4, 3, 2, 1, 4]
print(test.firstAndLastLargest(mylist))