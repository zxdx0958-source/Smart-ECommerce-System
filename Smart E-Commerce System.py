from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price 

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Error: Price cannot be negative!")
        else:
            self.__price = value

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def apply_discount(self):
        pass

class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def apply_discount(self):
        shipping_fee = self.weight * 5 
        return (self.price * 0.90) + shipping_fee

class DigitalProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def apply_discount(self):
        return self.price * 0.80

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.apply_discount()
        return total

def main():
    cart = ShoppingCart()
    store_products = [
        PhysicalProduct("Laptop", 1000, 2.5),
        DigitalProduct("Python Course", 50, "150MB"),
        PhysicalProduct("Headphones", 150, 0.3)
    ]

    while True:
        print("\n--- Smart E-Commerce System ---")
        print("1. View Available Products")
        print("2. Add Product to Cart")
        print("3. View Cart & Checkout")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Products:")
            for i, p in enumerate(store_products):
                print(f"{i+1}. {p.name} - ${p.price}")
        
        elif choice == "2":
            try:
                idx = int(input("Enter product number to add: ")) - 1
                if 0 <= idx < len(store_products):
                    cart.add_product(store_products[idx])
                    print(f"Added {store_products[idx].name} to cart.")
                else:
                    print("Error: Invalid product number.")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "3":
            if not cart.items:
                print("\nYour cart is empty.")
            else:
                print("\nYour Shopping Cart:")
                for item in cart.items:
                    print(f"- {item.name}")
                print(f"Final Total (after discounts & shipping): ${cart.calculate_total():.2f}")
        
        elif choice == "4":
            print("Thank you for using our system. Goodbye!")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()
