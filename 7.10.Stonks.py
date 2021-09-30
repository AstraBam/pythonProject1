stock = int(input())
purchase_price = 0
sale_price = 0
number = 0
while stock != 0:
    yesterday_stock = stock
    stock = int(input())
    if stock > yesterday_stock and number == 0:
        purchase_price = stock
        number += 1
    elif stock < yesterday_stock and number == 1:
        sale_price = stock
        number += 1
profit = sale_price - purchase_price
print(purchase_price, sale_price, profit)
