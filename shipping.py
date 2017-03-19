__author__ = 'Akriti Pun'

total_price = 0
final_total = 0

items = int(input("Enter number of items///"))

for i in range (items):
    items_price = float(input("Price of item:"))
    total_price += items_price

if total_price >= 100:
    discount = total_price * 0.10
    final_total = total_price - discount
print("Number of items {} total price of items ${:.2f}".format(items,final_total))
