class ItemToPurchase:
    """Represents an item that can be purchased."""

    def __init__(self, name="none", price=0.0, quantity=0,
                 description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def print_item_cost(self):
        """Print the item's quantity and total cost."""
        item_total = self.price * self.quantity
        print(
            f"{self.name} {self.quantity} @ "
            f"${self.price:.0f} = ${item_total:.0f}"
        )


class ShoppingCart:
    """Stores and manages a customer's shopping cart."""

    def __init__(self, customer_name="none",
                 current_date="January 1, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        """Add an item to the cart."""
        self.cart_items.append(item)

    def remove_item(self, item_name):
        """Remove the first item matching the given name."""
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                return

        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        """Update an item's quantity using a temporary item."""
        for item in self.cart_items:
            if item.name == modified_item.name:
                item.quantity = modified_item.quantity
                return

        print("Item not found in cart. Nothing modified.")

    def get_num_items(self):
        """Return the total quantity of all cart items."""
        return sum(item.quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        """Return the total cost of all cart items."""
        return sum(
            item.price * item.quantity
            for item in self.cart_items
        )

    def print_total(self):
        """Print the cart's items, quantities, and total cost."""
        print(f"{self.customer_name}'s Shopping Cart - "
              f"{self.current_date}")
        print(f"Number of Items: {self.get_num_items()}")
        print()

        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print("OUTPUT SHOPPING CART")
            for item in self.cart_items:
                item.print_item_cost()

        print()
        print(f"Total: ${self.get_cost_of_cart():.0f}")

    def print_descriptions(self):
        """Print the descriptions of all items in the cart."""
        print(f"{self.customer_name}'s Shopping Cart - "
              f"{self.current_date}")
        print()
        print("Item Descriptions")

        for item in self.cart_items:
            print(f"{item.name}: {item.description}")


def print_menu():
    """Display the menu and return a valid user command."""
    while True:
        print()
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()

        command = input("Choose an option:\n").strip().lower()

        if command in ("a", "r", "c", "i", "o", "q"):
            return command

        print("Invalid option. Please try again.")


def execute_menu(command, shopping_cart):
    """Execute the selected command for the shopping cart."""
    if command == "a":
        print("ADD ITEM TO CART")
        name = input("Enter the item name:\n").strip()
        description = input("Enter the item description:\n").strip()

        try:
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))

            if price < 0 or quantity < 0:
                print("Price and quantity cannot be negative.")
                return

            item = ItemToPurchase(
                name, price, quantity, description
            )
            shopping_cart.add_item(item)

        except ValueError:
            print("Invalid price or quantity. Item not added.")

    elif command == "r":
        print("REMOVE ITEM FROM CART")
        name = input("Enter name of item to remove:\n").strip()
        shopping_cart.remove_item(name)

    elif command == "c":
        print("CHANGE ITEM QUANTITY")
        name = input("Enter the item name:\n").strip()

        try:
            quantity = int(input("Enter the new quantity:\n"))

            if quantity < 0:
                print("Quantity cannot be negative.")
                return

            # A temporary object passes the name and new quantity.
            modified_item = ItemToPurchase(
                name=name,
                quantity=quantity
            )
            shopping_cart.modify_item(modified_item)

        except ValueError:
            print("Invalid quantity. Nothing modified.")

    elif command == "i":
        print("OUTPUT ITEMS' DESCRIPTIONS")
        shopping_cart.print_descriptions()

    elif command == "o":
        print("OUTPUT SHOPPING CART")
        shopping_cart.print_total()


def main():
    """Initialize the cart and run the interactive menu."""
    print("Enter Customer's Name:")
    customer_name = input().strip()

    print("Enter Today's Date:")
    current_date = input().strip()

    shopping_cart = ShoppingCart(customer_name, current_date)

    print()
    print("Customer Name:", shopping_cart.customer_name)
    print("Today's Date:", shopping_cart.current_date)

    while True:
        command = print_menu()

        if command == "q":
            break

        execute_menu(command, shopping_cart)

    print("Thank you for using the Shopping Cart System!")


if __name__ == "__main__":
    main()