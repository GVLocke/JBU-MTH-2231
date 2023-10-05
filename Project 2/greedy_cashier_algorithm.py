class Solution(object):
    def cashierAlgorithm(self, cents):    
        """Takes an integer number of cents and returns the corresponding denominations according to the greedy cashier's algorithm"""
        coins = [("Quarters", 25), ("Dimes", 10), ("Nickels", 5), ("Pennies", 1)]
        for coin, value in coins: # iterate through coins storing the string of each tuple as coin and the integer as value
            count = cents // value # set count to equal the integer part of cents/value
            if count > 0:
                print(f"{coin}: {count}") # print the number of coins
                cents -= count * value # remove the correct number of cents from the total cents

# test code
test = Solution()
test.cashierAlgorithm(37)