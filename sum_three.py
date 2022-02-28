
# Find the sum of three digit number.  113=5

num=int(input("enter three digit number:\n"))

a=num
sum=0
rem=num%10
sum=sum+rem
num=num//10

rem=num%10
sum=sum+rem
num=num//10

rem=num%10
sum=sum+rem
num=num//10

print("sum of digits is:",sum)