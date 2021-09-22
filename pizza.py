#importing an entire module
def make_pizza(size,*toppings):
	print(f"making a {size}-inch pizza with the following topping:")
	for topping in toppings:
		print(f"-{topping}")

