class Cart():
    def __init__(self):
        self.user_cart = []

    
    def show(self):
        if self.user_cart == []:
            print("Your cart is empty!")
        else:
            print(self.user_cart)
            print("These are the items in your cart")
    
    
    def add(self, item):
        if item.lower() not in self.user_cart:
            self.user_cart.append(item)
            print(f"{item} added to your cart!")
        elif item.lower() in self.user_cart:
            print("That's already in your cart.")


    def delete(self, item):
        if self.user_cart == []:
            print("Your cart is empty")
        else:
            print(f"Here are your cart items: {self.user_cart}")
            item = input("What would you like to delete?")
            if item in self.user_cart:
                self.user_cart.remove(item)
                print(f"{item} has been removed from your cart.")
            else:
                print("That didn't work, try a new command.")

    def clear_cart(self):
        final_ans = input("Are you sure you want to clear all items in your cart? <yes/no>")
        if final_ans.lower() == "yes":
            self.user_cart.clear()
            print("Your cart has been cleared.")
        elif final_ans.lower() == "no":
            pass


the_cart = Cart()

while True:
    command = input("Please enter a command: <show/add/delete/clear/quit>")
    
    if command.lower() == "show":
        the_cart.show()

    elif command.lower() == "add":
        item = input("What would you like to add to your cart?")
        the_cart.add(item)

    elif command.lower() == 'delete':
        the_cart.delete(item)

    elif command.lower() == "clear":
        the_cart.clear_cart()

    elif command.lower() == 'quit':
        break