
P = float(input("Enter the principal loan ammount: ") )
r = float(input("Enter the monthly interest rate (annual interest rate divided by 12 months): "))
n = float(input("Enter the total number of months of the loan: "))
M = P*(r*(1+r)**n) / ((1+r)**n - 1)
print("The monthly payment is: ", M)
