"""5. String and number manipulation:
a) Take two inputs from the user. Budget amount and percentage allocation.
b) Budget amount will be entered as $5000.00 and percentage as 20%.
c) Store them in two float variables (ignoring $ and % signs).
d) Calculate the total allocation amount (budget * percentage).
"""

budgetAmt = input(f"Please enter budget amount: ")
allocationPercentage = input(f"Please input the percentage of budget need to allocate: ")
budgetAmt = float(budgetAmt.removeprefix('$'))
print( f"The allocated budeget amount is $ {budgetAmt}")
allocationPercentage = float(allocationPercentage.removesuffix('%'))
print(f"The allocated percentage is {allocationPercentage}%")
totalAllocationAmt = (budgetAmt * allocationPercentage)/100
print(f"The total alloacted amount is ${totalAllocationAmt}, Jitni chadar utne hi pair falaye. Ok greeb :)")