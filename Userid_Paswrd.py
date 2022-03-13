#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

User_Id_1="kalpana"
Password_1=1234

User_Id_2=input("Enter UserName")
Password_2=int(input("Enter Password"))

i=1

if(User_Id_1 != User_Id_2 and Password_1 != Password_2):
    while(i<=5):
         
        if(i>3):
            print("Terminate coz of more than 3 attempts")
            break


        User_Id_2=input("Enter UserName")
        Password_2=int(input("Enter Password"))

       
        if((User_Id_1 == User_Id_2) and (Password_1 == Password_2)):
            print("valid Credenitials")
            break
        else:
            i+=1
else:
    print("Login Successful")








    