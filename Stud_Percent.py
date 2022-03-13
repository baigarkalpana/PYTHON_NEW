#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.
#95 76 85 90 89   ,95,85,74,64,53

Total_Student=int(input("Enter Total Number of Students:"))

i=1

while(i<=Total_Student):
    print("\nEnter Marks of 5 subject for Student",i)


    Marathi=int(input("\nEnter Marks of Marathi_Subject:"))
    English=int(input("Enter Marks of English_Subject:"))
    Hindi=int(input("Enter Marks of Hindi_Subject:"))
    Maths=int(input("Enter Marks of Maths_Subject:"))
    History=int(input("Enter Marks of History_Subject:"))
    
    Total_Marks = Marathi+English+Hindi+Maths+History
    Average=Total_Marks/5
    Percentage=(Total_Marks/500)*100

    print("\nAverage of Student",i,"is:",Average)
    print("Percentage of Student",i,"is:",Percentage)
    print("\n\n")
    
    i+=1



