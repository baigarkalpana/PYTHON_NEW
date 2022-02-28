# Write a program to reverse three digit number.

num=int(input("Enter three digit number:"))

sum=0

sum=sum*10+num%10
num=num//10

sum=sum*10+num%10
num=num//10

sum=sum*10+num%10
num=num//10

print("Reverse Number is:",sum)