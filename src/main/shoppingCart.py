class ShoppingCart():

    def __init__(self):
        self.total = 0
        self.cart = {}
    #i want to be able to add items to the cart
    def add_items(self, item_name, quantity, price):
        self.cart[item_name] = quantity
        self.total +=  price * quantity
    
    def remove_items(self, item_name, quantity, price):
        if(quantity < self.cart[item_name] and quantity >= 0):  
            self.cart[item_name] -= quantity
        elif(quantity >= self.cart[item_name]):
            del self.cart[item_name]
    
    def check_out(self, cash_paid):
        if (cash_paid >= self.total):
            return cash_paid - self.total
        else:
            return "Insufficient funds being paid."

    


