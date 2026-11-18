snack="biscuits"
price=5
is_available=True
quantity=10

print("Snack:", snack)
print("Price:", price)
print("Available:", is_available)
print("Quantity:", quantity)

print("The type of snack is:", type(snack))
print("The type of price is:", type(price))
print("The type of is_available is:", type(is_available))
print("The type of quantity is:", type(quantity))

total_cost = price * quantity
print("Total cost of", quantity, snack, "is:", total_cost)

print("Is the snack available?", is_available)
print("Is the price under 2?", price < 2)
print("Is the quantity greater than 5?", quantity > 5)

shop_name="Snack"+"Shop"
print("Shop Name:", shop_name)

print("The first character of the snack name is:", snack[0])

price_a=10
price_b=15
temp_price=price_a
price_a=price_b
price_b=temp_price

print("After swapping, price_a is:", price_a)
print("After swapping, price_b is:", price_b)