item_quatity=int(input("Enter item quatity:"))
item_price=int(input("Enter item price:"))
total_price=(item_quatity) * (item_price)
print(f"total_price:{total_price}")
discount_price=total_price/10
print(f"discount price:{discount_price}")
pay_amount=(total_price) - (discount_price)
print(f"The total amount to pay:{pay_amount}")

                   