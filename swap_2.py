# Assign two number and swap it without using third variable.

print("Enter two numbers for Swapping")

num1=int(input())
num2=int(input())

print("Before swapping num1 =",num1,"num2 =",num2)

num1,num2=num2,num1

print("After swapping num1 =",num1,"num2 =",num2)