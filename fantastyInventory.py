# Author Jacob Kenyon
# Create an inventory using a dictionary as the inventory model e.g.. {"Item name": amount}

stuff = {"Rope": 3, "Torch": 7, "Knife": 2, "Soup": 3,
         "Bread": 2, "Water": 6, "Gold Coin": 378,
         "Bronze Coin": 1226, }

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0

    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("\nTotal number of items: " + str(item_total))

displayInventory(stuff)