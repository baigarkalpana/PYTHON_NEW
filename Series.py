#Write a program to print the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)


n=int(input("Enter Number:"))

fact,sum=1,0
i=1
while(i<=n):
    f = 1
    Sum = 0
  
  
    for i in range(1, n + 1):
        f = f * i
        Sum += f

    i+=1
print("\nAddition of Series 1:",Sum)    

# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

no=int(input("\nEnter Number:"))


i=1
r=0
Sum1=0

while(i<=no):
    for i in range(1, no + 1):
        r = no ** i
        Sum1 += r

    i+=1


print("\nAddition of Series 2:",Sum1)




