class Solution(object):
    def bubblesort(self, list):
        """Takes in a list of n integers and sorts them using the bubblesort algorithm."""
        for i in reversed(range(len(list))):
            for j in range(i):
                if list[j] > list[j+1]:
                    temp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = temp

# test code
mylist = [26, 81, 83, 61, 52, 49, 74, 5, 49, 65, 43, 79, 56, 63, 47, 68, 6, 96, 83, 29]
print(f"Unordered list: {mylist}")
test = Solution()
test.bubblesort(mylist)
print(f"Ordered list: {mylist}")