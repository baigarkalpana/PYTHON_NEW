#Addition of Digits

num1=int(input("Enter number "))

x=num1//10
y=num1%10

add=x+y

print("Addition of two digits:",add)

#Addition of Digits more than two


num=int(input("Enter number "))

sum=0
number=num

while(num>0):

    rem=num%10
    sum=sum+rem

    num=num//10

print("Sum of Digits:",sum)    


























