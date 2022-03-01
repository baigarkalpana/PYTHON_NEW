#WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.


print("Enter Basic Salary & PF of an Employee ")

Basic=float(input())
PF=float(input())

DA= Basic * 0.1
TA= Basic * 0.12
HRA= Basic * 0.15


PF=Basic*(PF/100)

Total=Basic+DA+HRA+TA-PF

print(Total)