print("=== Pet Grooming Service Calculator ===")
print("Enter service package: bath, trim, or full")
print("Type 'done' when finished selecting services")

total = 0

while True:
    service = input("\nEnter service package: ")

    if service == "bath":
        price = 15
    elif service == "trim":
        price = 25
    elif service == "full":
        price = 40
    elif service == "done":
        break
    else:
        print("Invalid package!")
        continue

    total = total + price

    print(f"Price: ${price:.2f}")
    print(f"Current total: ${total:.2f}")

discount = total * 0.15
final_total = total - discount

print("\n=== Service Summary ===")
print(f"Subtotal: ${total:.2f}")
print(f"Multi-Pet Discount: -${discount:.2f}")
print(f"Final Total: ${final_total:.2f}")
print("Thank you for choosing our salon!")