print("=" * 50)
print("Question 2: Shopping cart")
print("=" * 50)

cart = ["apple", "banana", "milk", "bread", "eggs", "apple", "milk"]

apple_count = cart.count("apple")
print("Number of apples in the cart:", apple_count)

milk_position = cart.index("milk")
print("Position of milk in the cart:", milk_position)

cart.remove("apple")
removed_item = cart.pop()
print("Removed item using pop:", removed_item)

print("Is bannana in the cart?", "banana" in cart)
print("Final cart:", cart)
print()