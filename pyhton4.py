class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self,item_name,price):
        self.items[item_name] = price
        
    def update_item(self,item_name,price):
        self.items[item_name] = price
        
    def show_items(self):
        for item_name , price in self.items.items():
            print(f'{item_name}: ${price}')
    
    def total_price(self):
        total_price = 0
        for item_name in self.items:
            total_price += self.items[item_name]
        return total_price

def default_test():
    cart = Cart()
    cart.add_item("Apple", 1.5)
    cart.add_item("Banana", 0.5)
    cart.update_item("Apple", 2.0)
    cart.show_items()
    print("Total price:", cart.total_price())