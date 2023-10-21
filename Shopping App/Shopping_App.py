class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = {}

    def add_to_cart(self, product_id, quantity):
        for product in products:
            if product.product_id == product_id:
                if product_id in self.cart:
                    self.cart[product_id] += quantity
                else:
                    self.cart[product_id] = quantity
                print(f"{quantity} {product.name} added to your cart.")
                return
        print("Product not found.")

    def remove_from_cart(self, product_id, quantity):
        if product_id in self.cart:
            if self.cart[product_id] >= quantity:
                self.cart[product_id] -= quantity
                if self.cart[product_id] == 0:
                    del self.cart[product_id]
                print(f"{quantity} items removed from your cart.")
            else:
                print("Quantity to remove exceeds what's in your cart.")
        else:
            print("Product not in your cart.")

    def view_cart(self):
        print("Your Cart:")
        for product_id, quantity in self.cart.items():
            product = next((p for p in products if p.product_id == product_id), None)
            if product:
                print(f"{product.name} - Quantity: {quantity}")
            else:
                print("Product not found in the catalog.")

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_product(self, product):
        products.append(product)
        print(f"Product '{product.name}' added to the catalog.")
        write_data_to_file()

    def modify_product(self, product_id, new_name, new_category, new_price):
        for product in products:
            if product.product_id == product_id:
                product.name = new_name
                product.category = new_category
                product.price = new_price
                print(f"Product '{product.name}' modified.")
                write_data_to_file()
                return
        print("Product not found.")

    def remove_product(self, product_id):
        for product in products:
            if product.product_id == product_id:
                products.remove(product)
                print(f"Product '{product.name}' removed from the catalog.")
                write_data_to_file()
                return
        print("Product not found.")

    def add_category(self, category):
        categories.append(category)
        print(f"Category '{category}' added.")
        write_data_to_file()

    def remove_category(self, category):
        if category in categories:
            categories.remove(category)
            print(f"Category '{category}' removed.")
            write_data_to_file()
        else:
            print("Category not found.")

def read_data_from_file():
    try:
        with open("ecommerce_data.txt", "r") as file:
            lines = file.readlines()
            products = []
            categories = set()
            reading_products = True
            for line in lines:
                if reading_products:
                    if line.strip() == "":
                        reading_products = False
                    else:
                        parts = line.strip().split(",")
                        if len(parts) == 4:
                            product_id, name, category, price = parts
                            products.append(Product(int(product_id), name, category, float(price)))
                else:
                    categories.add(line.strip())
        return products, list(categories)
    except FileNotFoundError:
        return [], []

def write_data_to_file():
    with open("ecommerce_data.txt", "w") as file:
        for product in products:
            file.write(f"{product.product_id},{product.name},{product.category},{product.price}\n")
        file.write("\n")
        for category in categories:
            file.write(f"{category}\n")

# Define product catalog and categories
products, categories = read_data_from_file()

print("Welcome to the Demo Marketplace")

# Create user and admin accounts
users = [User("user1", "password1")]
admin = Admin("admin", "adminpassword")

while True:
    print("\n1. User Login")
    print("2. Admin Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        # User login logic
        user = None
        for u in users:
            if u.username == username and u.password == password:
                user = u
                break

        if user is not None:
            print("Logged in as User")
            while True:
                print("\nUser Menu:")
                print("1. View Cart")
                print("2. Add to Cart")
                print("3. Remove from Cart")
                print("4. Checkout")
                print("5. Logout")

                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    print("Your Cart:")
                    for product_id, quantity in user.cart.items():
                        product = next(p for p in products if p.product_id == product_id)
                        print(f"{product.name} - Quantity: {quantity}")

                elif user_choice == "2":
                    product_id = int(input("Enter the product ID to add to your cart: "))
                    quantity = int(input("Enter the quantity: "))
                    user.add_to_cart(product_id, quantity)

                elif user_choice == "3":
                    product_id = int(input("Enter the product ID to remove from your cart: "))
                    quantity = int(input("Enter the quantity to remove: "))
                    user.remove_from_cart(product_id, quantity)

                elif user_choice == "4":
                    print("Your order is successfully placed")

                elif user_choice == "5":
                    break

        else:
            print("Invalid credentials")

    elif choice == "2":
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")

        # Admin login logic
        if admin_username == admin.username and admin_password == admin.password:
            print("Logged in as Admin")
            while True:
                print("\nAdmin Menu:")
                print("1. Add Product")
                print("2. Modify Product")
                print("3. Remove Product")
                print("4. Add Category")
                print("5. Remove Category")
                print("6. Logout")

                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    product_id = len(products) + 1
                    product_name = input("Enter product name: ")
                    product_category = input("Enter product category: ")
                    product_price = float(input("Enter product price: "))
                    new_product = Product(product_id, product_name, product_category, product_price)
                    admin.add_product(new_product)

                elif admin_choice == "2":
                    product_id = int(input("Enter the product ID to modify: "))
                    new_name = input("Enter new product name: ")
                    new_category = input("Enter new product category: ")
                    new_price = float(input("Enter new product price: "))
                    admin.modify_product(product_id, new_name, new_category, new_price)

                elif admin_choice == "3":
                    product_id = int(input("Enter the product ID to remove: "))
                    admin.remove_product(product_id)

                elif admin_choice == "4":
                    new_category = input("Enter new category: ")
                    admin.add_category(new_category)

                elif admin_choice == "5":
                    category = input("Enter the category to remove: ")
                    admin.remove_category(category)

                elif admin_choice == "6":
                    break

        else:
            print("Invalid admin credentials")

    elif choice == "3":
        write_data_to_file()
        break
