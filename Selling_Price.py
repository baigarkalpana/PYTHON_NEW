
#WAP to calculate selling price of book based on cost price and discount.


#Selling price = Marked/List price – Discount.


cost=int(input("Cost Price of a Book is:"))
discount=int(input("discount on book is:"))


discount=discount/100

num=cost * discount

selling_price=cost-num


print("\nSelling Price is:",selling_price)