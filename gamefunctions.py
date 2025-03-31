# Steven Bartoldus
# 3/30/24
# Game Functions

"""Game functions for a Pokemon-style adventure game.

The functions welcome the player, display a shop menu, generate random monsters, and handle save/load functionality.
"""

import random
import json


def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
    """Handles item purchasing and calculates remaining money."""
    max_affordable = int(startingMoney // itemPrice)
    quantity_purchased = min(quantityToPurchase, max_affordable)
    remaining_money = round(startingMoney - (quantity_purchased * itemPrice), 2)
    return quantity_purchased, remaining_money


def new_random_monster():
    """Generates a random Pokemon with stats like health, power, and money."""
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


def print_welcome(name: str):
    """Displays a welcome message."""
    print(f"{'Hello, ' + name + '!':^20}")


def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """Displays a shop menu with two items."""
    print("+" + "-" * 22 + "+")
    print(f"| {item1Name:<12}${item1Price:>6.2f} |")
    print(f"| {item2Name:<12}${item2Price:>6.2f} |")
    print("+" + "-" * 22 + "+")


def save_game(filename: str, inventory: dict, money: float):
    """Saves game state to a JSON file."""
    with open(filename, 'w') as file:
        json.dump({"inventory": inventory, "money": money}, file)
    print("Game saved successfully.")


def load_game(filename: str) -> tuple:
    """Loads game state from a JSON file."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data.get("inventory", {}), data.get("money", 0.0)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Failed to load game. Starting a new game.")
        return {}, 0.0


def test_functions():
    """Tests all functions and displays output."""
    for name in ["Ash", "Misty", "Brock"]:
        print_welcome(name)

    for items in [
        ("Pokeball", 25.00, "Greatball", 50.00),
        ("RazzBerry", 15.00, "NanabBerry", 25.00),
        ("Antidote", 20.00, "Awakening", 25.00)
    ]:
        print_shop_menu(*items)

    for _ in range(3):
        monster = new_random_monster()
        print("\nMonster Generated:")
        for key, value in monster.items():
            print(f"{key}: {value}")

    items_bought, remaining_cash = purchase_item(30.0, 100.0, 3)
    print(f"\nPurchased {items_bought} items, remaining money: ${remaining_cash}")

if __name__ == "__main__":
    test_functions()


