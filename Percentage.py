
#Write a program to calculate the percentage of student based on marks of any 5 subjects.

Marathi_Sub=float(input("enter marks for subject Marathi"))
English_sub=float(input("enter marks for subject English"))
History_sub=float(input("enter marks for subject History"))
Hindi_sub=float(input("enter marks for subject Hindi"))
Maths_sub=float(input("enter marks for subject Maths"))


Total_Marks=Marathi_Sub + English_sub + Hindi_sub + Hindi_sub + Maths_sub
print("Total Marks  is:",Total_Marks)

Percentage=(Total_Marks / 500.0) *100

print("Percentage is:",Percentage)
