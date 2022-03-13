#Accept no. of passengers from user and per ticket cost. Then accept age of each.passenger and then 
# calculate total amount to ticket to travel for all of them based onfollowing condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

Total_Passengers=int(input("Total Number Of Passengers:"))
Ticket=int(input("Enter Ticket Amount:"))

i=1

while(i<=Total_Passengers):
    print("\nCalculation of Passenger:",i)
    Age=int(input("Enter Age of Passenger:"))

    if(Age < 12):
        Discount_K= Ticket * 0.3
        Total_K= Ticket-Discount_K
        print("\nPassenger",i, "gets 30 Percent Discount,Amount is:",Total_K)

    elif(Age > 59 ):
        Discount_K= Ticket * 0.5
        Total_K= Ticket-Discount_K
        print("\nPassenger",i, "gets 30 Percent Discount,Amount is:",Total_K)

       
    else:
        print("\nNo Discount For Passenger:",i,"Amount is:",Ticket)    

    i+=1