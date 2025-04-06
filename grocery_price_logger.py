# grocery_price_logger.py

def collect_grocery_items():
    groceries = []
    print("Enter grocery items and their prices per pound.")

    while True:
        name = input("Enter grocery name (or 'done' to finish): ")
        if name.lower() == 'done':
            break

        try:
            price = float(input(f"Enter the price of {name} per pound: "))
            groceries.append((name, price))
        except ValueError:
            print("Invalid input. Please enter a numeric value for price.")

    return groceries

def save_to_file(groceries, filename="grocery_price.txt"):
    with open(filename, "w") as file:
        for item, price in groceries:
            file.write(f"{item}, Price: ${price:.2f} per pound\n")

def display_file(filename="grocery_price.txt"):
    print("\n--- Grocery Price List ---")
    with open(filename, "r") as file:
        print(file.read())

def main():
    groceries = collect_grocery_items()
    if groceries:
        save_to_file(groceries)
        display_file()
    else:
        print("No items were entered.")

if __name__ == "__main__":
    main()