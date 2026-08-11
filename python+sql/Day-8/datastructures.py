from collections import deque


inventory = {
    "Laptop": {"price": 50000, "quantity": 5, "category": "Electronics"},
    "Mouse": {"price": 1000, "quantity": 10, "category": "Accessories"},
    "Keyboard": {"price": 2000, "quantity": 7, "category": "Accessories"}
}


recent_products = []

order_queue = deque()


def add_product(name, price, quantity, category):
    inventory[name] = {
        "price": price,
        "quantity": quantity,
        "category": category
    }

    recent_products.append(name)
    print(f"{name} added to inventory.")


def display_inventory():
    print("\n----- Inventory -----")

    for index, (name, details) in enumerate(inventory.items(), start=1):
        print(
            f"{index}. {name} | "
            f"Price: ₹{details['price']} | "
            f"Quantity: {details['quantity']} | "
            f"Category: {details['category']}"
        )


def add_order(product_name, quantity):
    order_queue.append((product_name, quantity))
    print(f"Order added: {product_name} x {quantity}")


def process_order():
    if not order_queue:
        print("No pending orders.")
        return

    product_name, quantity = order_queue.popleft()

    if product_name not in inventory:
        print("Product not found.")
        return

    if inventory[product_name]["quantity"] < quantity:
        print("Insufficient stock.")
        return

    inventory[product_name]["quantity"] -= quantity

    print(
        f"Order processed: "
        f"{product_name} x {quantity}"
    )


add_product("Monitor", 15000, 4, "Electronics")
add_product("Headphones", 3000, 8, "Accessories")

display_inventory()

add_order("Laptop", 2)
add_order("Mouse", 3)

print("\n----- Processing Orders -----")
process_order()
process_order()

display_inventory()


print("\n----- Recently Added Products -----")
while recent_products:
    print(recent_products.pop())


categories = {
    details["category"]
    for details in inventory.values()
}

print("\nUnique Categories:")
print(categories)