inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_Loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']



def display_inventory(inventory):
    print("Player Inventory: ")
    all_items = 0
    for k, v in inventory.items():
        print(k + " : " , v)
        all_items = all_items + v
    print("Number of all items: " , all_items)



def add_to_inventory(inventory, loot):
    for i in range(len(loot)):
         if(loot[i] in inventory.keys()):
             inventory[loot[i]] = inventory[loot[i]] + 1
         else:
             inventory[loot[i]] = 1
  
        


display_inventory(inventory)
print("------------------------------------------------")
print()

add_to_inventory(inventory, dragon_Loot)

display_inventory(inventory)
