#Addition of Three Digits
''' n=int(input("Enter three digit Number"))
print("\n Your Entered Value is:",n)

sum=0
rem1=n%10
sum=sum+rem1
n=n//10


rem2=n%10
sum=sum+rem2
n=n//10

rem3=n%10
sum=sum+rem3
n=n//10

print(sum)
'''
#Reverse the number
'''
print("enter number to Reverse")
num=int(input())
n=num

rev=0

while(num>0):
    rev=rev*10+num%10
    num=num//10

print("Reverse Number of :-",n ,"is",rev)    
'''

'''
x,y,z=11,21,1

if(x>y):
    if(x>z):
        print(x)
    else:
        print(z)
else:
    if(y>z):
        print(y)
    else:
        print(z)                



if(10>20):
    print(True)

else:
    print(False)    

'''

#using elif working as a SwitchCase
'''
print("Enter Your Number:")
no=int(input())

if(no == 0):
    print("ZERO")
elif(no==1):
    print("ONE")

elif(no == 2):
    print("TWO")

elif(no == 3):
    print("THREE")

elif(no ==4):
    print("FOUR")

elif(no ==5):
    print("FIVE")

elif(no ==6):
    print("SEVEN")

else:
    print("Invalid")     
'''

print("Enter Two Numbers:")

no1=int(input())
no2=int(input())

result=0

op=input("Enter your Choice: \n 1.** \n 2.// \n 3.% \n 4.+ \n 5.- ")

if(op == "+"):
    result=no1+no2
elif(op == "**"):
    result=no1**no2
elif(op == "//"):
    result=no1//no2
elif(op == "-"):
    result=no1-no2
elif(op== "%"):
    result=no1%no2

else:
    print("Invalid Operator")        

print("Result is:",result)


























































