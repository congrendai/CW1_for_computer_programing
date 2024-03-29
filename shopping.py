import json
import time
import datetime
from datetime import date

class Product():
    def __init__(self, name = None, price = None, quantity = None, unique_identifier = None, brand = None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.unique_identifier = unique_identifier
        self.brand = brand
    
    # Return JSON format of the object
    def to_json(self):
        return json.dumps(self.__dict__)

class Clothing(Product):
    def __init__(self, name = None, price = None, quantity = None, unique_identifier = None, brand = None, size = None, material = None):
        super().__init__(name, price, quantity, unique_identifier, brand)
        self.size = size
        self.material = material

class Food(Product):
    def __init__(self, name = None, price = None, quantity = None, unique_identifier = None, brand = None, expiry_date = None, gluten_free = None, suitable_for_vegans = None):
        super().__init__(name, price, quantity, unique_identifier, brand)
        self.expiry_date = expiry_date
        self.gluten_free = gluten_free
        self.suitable_for_vegans = suitable_for_vegans

class Phone(Product):
    def __init__(self, name = None, price = None, quantity = None, unique_identifier = None, brand = None, model = None, storage = None):
        super().__init__(name, price, quantity, unique_identifier, brand)
        self.model = model
        self.storage = storage

class ShoppingCart():
    def __init__(self, products = []):
        self.__products = products

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product):
        self.__products.remove(product)

    def get_contents(self):
        return sorted(self.__products, key = lambda x: x.name)

    def change_product_quantity(self, product, quantity):
        product.quantity = quantity

# This method uses to get attributes values and varifiy the values for products
# Then, return a product with attributes
def get_value(product):
    for key in vars(product).keys():

        # Get price and check if it is a float number
        if key == "price": 
            temp = "price (£)"
            while True:
                try:
                    # Check if the input is a float
                    value = float(input("Insert its {}: ".format(temp)))
                    break
                except: print("You should enter a float number.")
            setattr(product, key, value)
        
        # Get quantity and storage and check if it is an integer and greater than 0
        elif key == "quantity" or key == "storage": 
            while True:
                try:
                    # Check quantity cannot be 0 and if the input is a integer
                    value = int(input("Insert its {} (>=1): ".format(key)))
                    if value > 0:
                        break
                    else: print("The number cannot be 0!")
                except: print("You should enter an integer number.")  
            setattr(product, key, value)

        # Get unique_identifier and check if it is an digit sequamce string, 
        # a 13-digits sequence, uniqueness
        elif key == "unique_identifier": 
            temp = "EAN code"
            while True:
                try:
                    value = input("Insert its {}: ".format(temp))
                    int(value)
                    # Check whether the EAN code is a 13 digit sequence
                    if len(value) != 13:
                        print("EAN code should be a 13 digit sequence")
                        # Check the uniqueness of the EAN code
                    elif value in EAN_code:
                        print("EAN code should be unique for each product.")
                    else:
                        EAN_code.add(value)
                        setattr(product, key, value)
                        break
                # Check whether the EAN code is a digit sequence
                except: print("EAN code should be a digit sequence")

        # Get expiry date and model with the format of "dd/mm/yyyy"
        # This checks whether the expiry date is older the today
        # and checks whether the format of date is valid
        elif key == "expiry_date":
            temp = "expiry date"
            while True:
                value = input("Insert its {} (dd/mm/yyyy): ".format(temp))
                try:
                    # Check whether the expiry date is older the today. If so, reenter the date
                    result = datetime.datetime.strptime(value, "%d/%m/%Y").date()
                    result = time.strptime(str(result), "%Y-%m-%d")
                    today = time.strptime(date.today().strftime("%d/%m/%Y"), "%d/%m/%Y")
                    if result >= today:
                        setattr(product, key, value)
                        break
                    else: print("Don't cling to the past!")
                except: print("The date format is wrong.")
        
        # Get gluten_free and suitable_for_vegans with the format of "Y" or "N"
        # Check the food is gluten free and suitable for vegans or not
        elif key == "gluten_free" or key == "suitable_for_vegans": 
            while True:
                temp = " ".join(key.split("_"))
                value = input("Is this product {} (Y/N): ".format(temp)).lower()
                if value == "y":
                    value = True
                    break
                elif value == "n":
                    value = False
                    break
                else: print("Please enter Y or N.")         
            setattr(product, key, value)
        else:
            # Check whether the input is empty for common attributes of products 
            # such as name, brand, size and material
            while True:
                value = input("Insert its {}: ".format(key))
                if value:
                    setattr(product, key, value)
                    break
                else: print("You havn't entered a value for {}".format(key))
    return product

# Check the cart whether is empty. If it's not, and then return the cart
def check_cart(shopping_cart):
    if shopping_cart: return shopping_cart
    else: print("The cart is empty.")

# This method uses to print common attributes of products 
# such as name, price, quantity, unique_identifier and brand
def basic_summary(dict):
    return "   {} - {} * {} = £{} \n      The EAN code is {}.".format(entry_num, dict["quantity"], dict["name"], dict["quantity"]*dict["price"], dict["unique_identifier"]), dict["quantity"]*dict["price"]
    
if __name__ == '__main__':

    # Register for classes of products
    types = {
        "clothing": Clothing(), 
        "food": Food(),
        "phone": Phone()
    }

    # Create a instance of the ShoppingCart class
    shopping_cart = ShoppingCart()
    EAN_code = set()

    # Information about starting shopping
    print('The program has started.')
    print('Insert your next command (H for help):')

    # Flag to stop the loop of the program
    terminated = False

    # Start looping the program
    while not terminated:
        c = input("Type your next command: ").lower()

        # This is for adding products to the cart
        if c == "a":
            type_input = input("Insert its type: ").lower()
            # Check whether clothing,food,phoen are correctly entered, case-insensitive
            if type_input in types.keys():
                for key, value in zip(types.keys(), types.values()):
                    if type_input == key:
                        product = value
                        shopping_cart.add_product(get_value(value))
                        print("The {} has been added to the cart.".format(product.name))
            else: print("Please enter {}.".format(", ".join(types.keys())))

        # This is for deleting product by EAN code from the cart
        elif c == "r":
            cart = check_cart(shopping_cart.get_contents())
            if cart:
                 while True:
                    EAN = input("Enter the EAN code for deleting the product: ")
                    if EAN in EAN_code:
                        for product in cart:
                            if vars(product)["unique_identifier"] == EAN:
                                shopping_cart.remove_product(product)
                                print("The {} has been removed from the cart.".format(product.name))
                                EAN_code.remove(EAN)
                                break
                        break
                    else: print("This EAN code doesn't exist.")

        # This is for printing the summary of the cart
        elif c == "s":
            cart = check_cart(shopping_cart.get_contents())
            if cart:
                entry_num = 0
                total = 0
                print("This is the total of the expenses:")
                for product in cart:
                    entry_num += 1
                    dict = vars(product)
                    # print summary according to poducts'attributes
                    if "expiry_date" in dict.keys(): 
                        summary, total_temp = basic_summary(dict)
                        print(summary)
                        print("      The expiry date is {}.".format(dict["expiry_date"]))
                        print("      Is it gluten free: {}.".format(dict["gluten_free"]))
                        print("      Is it suitable for vegans: {}.".format(dict["suitable_for_vegans"]))
                        total += total_temp
                    elif "model" in dict.keys():
                        summary, total_temp = basic_summary(dict)
                        print(summary)
                        print("      The model is {}.".format(dict["model"]))
                        print("      The storage is: {} GB.".format(dict["storage"]))
                        total += total_temp
                    elif "size" in dict.keys():
                        summary, total_temp = basic_summary(dict)
                        print(summary)
                        print("      The size is {}.".format(dict["size"]))
                        print("      The material is: {}.".format(dict["material"]))
                        print("      This is made by {}.".format(dict["brand"]))
                        total += total_temp
                print("   Total = £{}".format(total))

        # This is for changing quantity of a product by EAN code in the cart
        elif c == "q":
            cart = check_cart(shopping_cart.get_contents())
            if cart:
                while True:
                    EAN = input("Enter the EAN code for changing the quantity of a product: ")
                    if EAN in EAN_code: break
                    else: print("This EAN code doesn't exist.")
                while True:
                    try:
                        quantity = int(input("Enter the quantity (>1): "))
                        break
                    except: print("Please enter an integer number.")
            for product in cart:
                if vars(product)["unique_identifier"] == EAN:
                    shopping_cart.change_product_quantity(product, quantity)
                    print("The quantity changed to {}".format(quantity))

        # This is for print cart to JSON format 
        elif c == "e":
            cart = check_cart(shopping_cart.get_contents())
            if cart:
                print("\nThe JSON format of the cart:\n")
                json_dict = {}
                for product in cart:
                    json_dict[product.name] = json.loads(product.to_json())
                print(json.dumps(json_dict, indent = 4))
        
        # Quit the programme
        elif c == "t": terminated = True

        # Show help
        elif c == "h":
            print("The program supports the following commands:")
            print("   [A] - Add a new product to the cart")
            print("   [R] - Remove a product from the cart")
            print("   [S] - Print a summary of the cart")
            print("   [Q] - Change the quantity of a product")
            print("   [E] - Export a JSON version of the cart")
            print("   [T] - Terminate the program")
            print("   [H] - List the supported commands")
        else: print("Command not recognised. Please try again.")
    print('Goodbye.')