# Steven Bartoldus
# 3/30/24
# Game Functions

"""Game functions for a Pokemon-style adventure game.

The functions welcome the player, display a shop menu, generate random monsters, and handle save/load functionality.
"""

import random
import json

def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
    max_affordable = int(startingMoney // itemPrice)
    quantity_purchased = min(quantityToPurchase, max_affordable)
    remaining_money = round(startingMoney - (quantity_purchased * itemPrice), 2)
    return quantity_purchased, remaining_money

def new_random_monster():
    monsters = [
        {"name": "Snorlax", "description": "A sleepy Pokemon blocking your path.", "health_range": (220, 280), "power_range": (70, 110), "money_range": (30, 130)},
        {"name": "Charizard", "description": "A dragon-like Pokemon with fire breath.", "health_range": (150, 250), "power_range": (80, 120), "money_range": (50, 150)},
        {"name": "Mewtwo", "description": "A powerful psychic Pokemon.", "health_range": (200, 330), "power_range": (170, 220), "money_range": (40, 170)}
    ]
    monster = random.choice(monsters)
    return {
        "name": monster["name"],
        "description": monster["description"],
        "health": random.randint(*monster["health_range"]),
        "power": random.randint(*monster["power_range"]),
        "money": round(random.uniform(*monster["money_range"]), 2)
    }

def equip_item(inventory, item_type):
    relevant_items = [item for item in inventory if item['type'] == item_type]

    if not relevant_items:
        print(f"No {item_type}s to equip.")
        return None

    print("Available items to equip:")
    for index, item in enumerate(relevant_items, start=1):
        print(f"{index}) {item['name']}")

    item_choice = input("Select an item to equip: ").strip()
    try:
        item_choice = int(item_choice) - 1
        if 0 <= item_choice < len(relevant_items):
            for item in inventory:
                item['equipped'] = False
            equipped_item = relevant_items[item_choice]
            equipped_item['equipped'] = True
            print(f"{equipped_item['name']} equipped!")
            return equipped_item['name']
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Invalid input. Please select a valid item.")
        return None

def use_auto_defeat_item(inventory: list):
    for item in inventory:
        if item.get("type") == "consumable" and item.get("effect") == "auto-defeat":
            inventory.remove(item)
            print("The Mewtwo Saber activates and defeats the monster!")
            return True
    return False

def print_welcome(name: str):
    print(f"{'Hello, ' + name + '!':^20}")

def print_shop_menu(items):
    print("+" + "-" * 22 + "+")
    for item1, price1, item2, price2 in items:
        print(f"| {item1:<15} ${price1:>6.2f} | {item2:<15} ${price2:>6.2f} |")
    print("+" + "-" * 22 + "+")

def save_game(filename: str, inventory: dict, money: float):
    with open(filename, 'w') as file:
        json.dump({"inventory": inventory, "money": money}, file)
    print("Game saved successfully.")

def load_game(filename: str) -> tuple:
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data.get("inventory", []), data.get("money", 0.0)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Failed to load game. Starting a new game.")
        return [], 0.0

def test_functions():
    for name in ["Ash", "Misty", "Brock"]:
        print_welcome(name)

    for items in [
        ("Quick Claw Knife", 50.00, "Mewtwo Saber", 75.00),
        ("Pokeball", 25.00, "Greatball", 50.00),
        ("RazzBerry", 15.00, "NanabBerry", 25.00),
        ("Antidote", 20.00, "Awakening", 25.00)
    ]:
        print_shop_menu([items])

    for _ in range(3):
        monster = new_random_monster()
        print("\nMonster Generated:")
        for key, value in monster.items():
            print(f"{key}: {value}")

    items_bought, remaining_cash = purchase_item(30.0, 100.0, 3)
    print(f"\nPurchased {items_bought} items, remaining money: ${remaining_cash}")

test_functions()


