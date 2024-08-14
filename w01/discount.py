from datetime import datetime

subtotal = 0
discount = 0

price = 1
while price != 0:
    price = float(input("Price: "))
    if price == 0:
        break
    quantity = int(input("Quantity: "))
    subtotal += price * quantity
    print(f"Current Subtotal: {round(subtotal, 2)}")
    print()

subtotal = round(subtotal, 2)

day_of_week = datetime.now().weekday()

if day_of_week == 1 or day_of_week == 2:
    if subtotal > 50:
        discount = subtotal * 0.1
        subtotal -= discount
    else:
        print(f"Additional amount to receive discount: {50 - subtotal}")

if discount:
    print(f"Discount amount: {round(discount, 2)}")

tax = round(subtotal * 0.06, 2)
print(f"Sales tax amount: {tax}")

total = round(subtotal + tax, 2)
print(f"Total: {total}")
