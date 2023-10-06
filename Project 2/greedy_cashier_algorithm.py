class Solution(object):
    def cashierAlgorithm(self, cents, denominations):
        """Takes an integer number of cents and returns the corresponding denominations according to the greedy cashier's algorithm
        Denominations argument must be a list of tuples with the following data:(String "Denomination Name", integer centValue)
        """
        for (
            coin,
            value,
        ) in (
            denominations
        ):  # iterate through coins storing the string of each tuple as coin and the integer as value
            count = cents // value  # set count to equal the integer part of cents/value
            if count > 0:
                print(f"{coin}: {count}")  # print the number of coins
                cents -= (
                    count * value
                )  # remove the correct number of cents from the total cents


# test code
test = Solution()
print("Select denominations to use or type 0 to continue: ")
options = [
    ("Pennies", 1),
    ("Nickels", 5),
    ("Dimes", 10),
    ("Quarters", 25),
    ("$1 Bills", 100),
    ("$5 Bills", 500),
    ("$10 Bills", 1000),
    ("$20 Bills", 2000),
    ("$50 Bills", 5000),
    ("$100 Bills", 10000),
]


for i, option in enumerate(options):
    print(f"{i+1}. {option[0]}")
selections = input(
    "Enter the numbers corresponding to the denominations you want to use, separated by commas: "
)
selections = selections.split(",")
selections = [int(s.strip()) for s in selections]
selected_denominations = [(options[i - 1][0], options[i - 1][1]) for i in selections]
dollars_cents = input("Enter a dollar amount (e.g. 12.34): ")
dollars, cents = dollars_cents.split(".")
cents = int(cents)
dollars = int(dollars)
total_cents = dollars * 100 + cents
test.cashierAlgorithm(total_cents, reversed(selected_denominations))
