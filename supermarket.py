# while product name not stop continue
product_name = input("please enter product name:")
sum_products = 0
products_counter = 0
max_price = 0
min_price = 10000
while product_name != "stop":
    product_price = float(input("please enter product price:"))
    products_counter += 1
    sum_products += product_price
    if product_price < min_price:
        min_price = product_price
    if product_price > max_price:
        max_price = product_price
    productName = input("please enter product name:")
print(f"{max_price}, {min_price}, {products_counter}")
print(f"max price: {max_price}")
print(f"min price: {min_price}")
print(f"products count: {products_counter}")

