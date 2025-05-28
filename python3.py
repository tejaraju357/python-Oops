class Inventory:
    def __init__ (self):
        self.products = {}
        
    def add_product(self,product_name,quantity):
        if product_name in self.products:
            self.products[product_name] += quantity
        else:
            self.products[product_name] = quantity
    
    def check_stock(self,product_name):
        if product_name in self.products:
            return self.products[product_name]
        else:
            return "Product not found"

def default_test():
    inventory = Inventory()
    inventory.add_product("Laptops", 10)
    inventory.add_product("Smartphones", 50)
    print(inventory.check_stock("Laptops"))  
    print(inventory.check_stock("Smartphones"))  