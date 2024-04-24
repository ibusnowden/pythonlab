number_of_books = int(input("How many books would you like to purchase? "))
base_price = float(input("What is the base price per book? $"))
total_cost = number_of_books * base_price
discount = total_cost * 0.1
cost_after_discount = total_cost - discount

print(f"Total cost before discount: ${total_cost}")
print(f"Discount: ${discount}")
print(f"Total cost after discount ${cost_after_discount}")
