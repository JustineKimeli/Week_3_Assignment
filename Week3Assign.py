#week 3 assignment
def calculate_discount(price,discount_percent):
    #checking if there is discount
    if discount_percent >=0.2:
        #calculate discount price
        discounted_price=price-(price*discount_percent)
        return discounted_price
    else:
       return price
# example
original_price=int(input("Enter the price of the item"))
discount_percent=0.3
final_price=calculate_discount(original_price,discount_percent)
#printing final price after applying discount
if final_price !=original_price:
   print("Final price after applying discount:", final_price)
else:
    print("Original price")
