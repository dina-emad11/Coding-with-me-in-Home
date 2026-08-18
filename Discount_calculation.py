Total_price = float(input("Enter your Total_price: "))
has_discount_card = input("Has discount card (Yes / No): ")
if Total_price >= 500 and has_discount_card == "Yes":
     discount_rate = 0.20
elif Total_price >= 500 or has_discount_card == "Yes":
    discount_rate = 0.10
else:
    discount_rate = 0.0
#discount_amount=total price * (discount rate/100
discount_amount = Total_price * discount_rate
final_price = Total_price - discount_amount

if discount_rate > 0:
    print("Discount amount: ",discount_amount)
    print("Final price: ",final_price)
else:
    print("Sorry, you don’t have a discount.")

