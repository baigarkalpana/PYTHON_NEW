#Write a program to print first 50 prime numbers.

for num in range(1,51):
       
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")