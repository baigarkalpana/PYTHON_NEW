num1=int(input("enter first number"))
num2=int(input("enter second number"))

op= input("enter operator")


if(op == "+"):
    result=num1+num2
    print("Result is:",result)

elif(op == "-"):
    result=num1-num2
    print("Result is:",result)

elif(op == "*"):
    result=num1*num2
    print("Result is:",result)

elif(op == "/"):
    result=num1/num2
    print("Result is:",result)

elif(op == "//"):
    result=num1//num2
    print("Result is:",result)

elif(op == "%"):
    result=num1%num2 
    print("Result is:",result)       

else:
    print("INVALID")




