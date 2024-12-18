def calculate_discount(price, discount_percent):
   return price*discount_percent/100

discount = 20

price=int(input("Enter price:"))
          
dis= int(input ("Enter discount:"))


if dis >= discount:
 print ("The final price is:", calculate_discount(price, dis))

else:
  print ("The final price is:", price)