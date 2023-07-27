
print("*** WELCOME TO OUR SHOPPING CART ***")
print("-"*45)
print("Treat me as your shopping list evaluator who will count all your items and display the final amount.")
item= input("What are you going to buy today?")
price = float(input(f"What is the price of {item} in dollars: "))
quantity = float(input(f"How many {item} are you buying?"))
print(f"Added {quantity} {item}(s) to your shopping cart")
print(f"Total amount is : $ {quantity*price}")
print("-"*45)
print("THANKS FOR SHOPPING WITH US")

# A simple project that taught me the use of f strings.





