"""
Requiremnets
Total rent
Total Paisa on Grocery
Total paisa on Sbji
Total paisa on Gas
"""
Rent=int(input("Enter the total amount: "))
Grocery=int(input("Enter the total amount of Grocery: "))
Sbji=int(input("Enter the total amount spent on Sbji: "))
Gas=int(input("Amount on Gas: "))
Electricity=int(input("Electricity bill: "))
Water=int(input("Water bill: "))
Person=int(input("Total number of person in Flat: "))
Expense=(Rent+Grocery+Sbji+Gas+Electricity+Water)//Person
print(f'Expense per person :',Expense)