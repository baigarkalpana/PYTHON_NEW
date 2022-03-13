# Write a program to check if given number is Armstrong number or not.
# Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3

Num=int(input("Enter Number:"))
Temp=Num
sum=0

while(Num!=0):
    digit=Num%10
    
    sum=sum+digit**3

    Num=Num//10

if(Temp==sum):
    print("\nGiven Number:",Temp,"is Armstrong Number")

else:
    print("\nGiven Number:",Temp,"is Not a Armstrong Number")

