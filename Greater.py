
#Find Greatest Number amongs the Three

print("Enter three Numbers:")

x=int(input())
y=int(input())
z=int(input())


if(x>y):
    if(x>z):
        print("Greatest Amongs the Three is:",x)
    else:
        print("Greatest Amongs the Three is:",z) 
else:
    if(y>z):
        print("Greatest Amongs the Three is:",y)
    else:
        print("Greatest Amongs the Three is:",z)               