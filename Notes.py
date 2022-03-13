#Write a program to accept an integer amount from user and tell minimum
#number of notes needed for representing that amount. (Use looping to optimise the problem)

num=int(input("Enter Number"))
sum=0

sum= num//100

rem1= num%100

sum=sum+rem1//50

rem2=rem1%50

print(sum)