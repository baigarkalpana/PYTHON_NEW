#Convert distant given in feet and inches into meter and centimeter

'''
15 ft = 15 × 0.3048 m = 4.572 m

3*2.54= inch to cm;
3 inch = 7.62 centimeter'''

feet=int(input("enter feet"))
inches=int(input("enter inches"))

f_meter=feet*0.3048
i_centimeter=inches*2.54

print("converted value of feet and inches are:",f_meter ,i_centimeter)

