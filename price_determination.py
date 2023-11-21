import random
import numpy as np
class Trash:
    cleaningType = None
    lowBidText = ["Your bid is too low. Please enter a higher bid: ", "Fair bid but that will not do. Please enter a higher value: ", "You are almost there. Please enter a higher bid: "]
    def __init__(self, size, quantity, package) ->  None:
        self.size = int(size)
        self.quantity = int(quantity)
        self.package = package #bucket -> 10, trash bag -> 27, wheelbarrow -> 80
        
    def calculate_volume(self, size, quantity) -> float:
        return (int(size)/1000) * int(quantity)
    
    def calculate_price(self, volume) -> float:
        print("CleaningType: "+str(self.cleaningType))
        if self.package is not self.cleaningType:
            return (volume * 0.05) * 1.2
        return volume * 0.05
    
    def bidding(self, bid) -> None:
        price = self.calculate_price(self.calculate_volume(self.size, self.quantity))
        print("System Price: "+str(price))
        while bid < price:
            bid = float(input(random.choice(self.lowBidText)))
        print("Your bid is accepted. You will be contacted shortly")

# End of Trash Class
        
class UI:
    def __init__(self) -> None:
        self.trash = None
    def display(self):
        details = np.array([])
        print("How would you like to dispose your trash?")
        print("1. Pickup my trash\n2. Pickup my trash and cleanup trash area")
        choice = int(input("Reply >> "))
        self.cleaningType = {1:"pickup", 2:"pickup and cleanup"}.get(choice, 1)
        print("Please select your disposal trash type")
        print("1. Bucket-10L\n2. Trash Bag-27L\n3. Wheelbarrow-80L")
        choice = int(input("Reply >> "))
        if choice == 1:
            details = np.append(details, ["bucket", 10])
        elif choice == 2:
            details = np.append(details, ["trash bag", 27])
        elif choice == 3:
            details = np.append(details, ["wheelbarrow", 80])
        quantity = int(input("How many of these do you have? "))
        details = np.append(details, quantity)
        self.trash = Trash(details[1], details[2], details[0])
        self.trash.cleaningType = self.cleaningType
# End of UI Class

ui = UI()
ui.display()
ui.trash.bidding(float(input("Enter your bid: ")))

