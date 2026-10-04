# Supermarket Billing System

items = {
    "rice": 60,
    "sugar": 45,
    "oil": 120,
    "milk": 30,
    "bread": 40,
    "eggs": 70,
    "biscuits": 30
}

cart = {}

print("===== SUPERMARKET BILLING SYSTEM =====")

while True:
    print("\nAvailable Items:")
    for item, price in items.items():
        print(item, "₹", price)

    choice = input("\nEnter item name (or 'done' to finish): ").lower()

    if choice == "done":
        break

    if choice in items:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            if choice in cart:
                cart[choice] += quantity
            else:
                cart[choice] = quantity

            print(quantity, choice, "added to cart.")
        else:
            print("Quantity must be greater than 0.")

    else:
        print("Item not available.")

# Generate bill
print("\n========== FINAL BILL ==========")

total = 0

if len(cart) == 0:
    print("Cart is empty.")
else:
    print("Item\t\tQty\tPrice\tAmount")

    for item, quantity in cart.items():
        price = items[item]
        amount = price * quantity
        total += amount

        print(f"{item.title():10}\t{quantity}\t₹{price}\t₹{amount}")

    print("--------------------------------")
    print("Total Amount: ₹", total)

print("Thank you for shopping!")