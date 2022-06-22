

from timeit import repeat
from turtle import goto


childrenmeal = float(input("What is the price of a child's meal? "))
adultsmeal = float(input("What is the the price of a adults's meal? "))
tax = float(input("What is the price of taxes? "))
percentage = float(input("Percentage over taxes:"))

print(f"The price of a child's meal: {childrenmeal} ")
print(f"The price of an adult's meal: {adultsmeal} ")
nc = input("The number of children? ")
na = input("The number of adults? ")
print(f"The sales tax rate: {tax} ")

tot = (childrenmeal* int(nc))+ adultsmeal* int(na)
print(f"Total: {tot}")
taxa = tot*tax/100
print(f"Total taxes: {taxa}")
print(f"Total price: {taxa + tot} ")

pay = input("What is the payment amount? ")
totaltotal = (int(pay) - (taxa + tot))

while  totaltotal < 0:
              print(f"insuficient. Remaining price: {totaltotal*-1}")
              paay = input("What is the payment amount?")
              totaltotal = ((int(pay)+int(paay)) - (taxa + tot))
print(f"Change: {  totaltotal}")
