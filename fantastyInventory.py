# Author Jacob Kenyon
# Create an inventory using a dictionary as the inventory model e.g.. {"Item name": amount}
# PART II : Create a looting system. (EXTREMELY SIMPLIFIED)

stuff = {"Rope": 3, "Torch": 7, "Knife": 2, "Soup": 3, "Bread": 2, "Water": 6,
         "Gold Coin": 378, "Bronze Coin": 1226, }

dragon_loot = ['Gold Coin', 'Gold Coin', 'Gold Coin', 'Bronze Coin', 'Bronze Coin', 'Rope', 'Dragon Claw', 'Dragon Claw', ]


# Takes a list of items and adds them to a dictionary containing the inventory.
def addToInventory(inventory, loot):
    for i in loot:
        if i not in inventory:
            inventory.setdefault(i, 1)
            print("Added one NEW " + i)
        else:
            inventory[i] += 1
            print("Added one " + i)


# Display the inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0

    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("\nTotal number of items: " + str(item_total))


# Code to Run
displayInventory(stuff)
addToInventory(stuff, dragon_loot)
displayInventory(stuff)


"""
OUTPUT:
Inventory:
3 Rope
7 Torch
2 Knife
3 Soup
2 Bread
6 Water
378 Gold Coin
1226 Bronze Coin

Total number of items: 1627
Added one Gold Coin
Added one Gold Coin
Added one Gold Coin
Added one Bronze Coin
Added one Bronze Coin
Added one Rope
Added one NEW Dragon Claw
Added one Dragon Claw
Inventory:
4 Rope
7 Torch
2 Knife
3 Soup
2 Bread
6 Water
381 Gold Coin
1228 Bronze Coin
2 Dragon Claw

Total number of items: 1635

Process finished with exit code 0
"""