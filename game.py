#    Steven Bartoldus
#    2/16/24
#    Game Functions

"""Game functions for a pokemon style adventure game.

The functions welcomes the player, displays a shop menu and generates a random monster.
"""


import random

def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
    """
    What can be purchased and the remaining money.

    Parameters:
        itemPrice (float): Cost per item.
        startingMoney (float): Player's available money.
        quantityToPurchase (int): Number of items the player wants to buy (default: 1).

    Returns:
        Number of items purchased and remaining money.

    """
    max_affordable = int(startingMoney // itemPrice)
    quantity_purchased = min(quantityToPurchase, max_affordable)
    remaining_money = round(startingMoney - (quantity_purchased * itemPrice), 2)
    
    return quantity_purchased, remaining_money


def new_random_monster():
    """
    Generates a random Pokemon with stats like health range, power range, and money range.
    
    Returns:
        A pokemon with a description, health, power and money

"""
    monsters = [
        {
            "name": "Snorlax",
            "description": "A sleepy pokemon blocking your path. It is angry when awoken.",
            "health_range": (220, 280),
            "power_range": (70, 110),
            "money_range": (30, 130),
        },
        {
            "name": "Charizard",
            "description": "A dragon-like pokemon, with strength, flight and fire.",
            "health_range": (150, 250),
            "power_range": (80, 120),
            "money_range": (50, 150),
        },
        {
            "name": "Mewtwo",
            "description": "A artificial psychic pokemon that is long and grey with a purple tail",
            "health_range": (200, 330),
            "power_range": (170, 220),
            "money_range": (40, 170),
        },
    ]
    
    monster = random.choice(monsters)
    return {
        "name": monster["name"],
        "description": monster["description"],
        "health": random.randint(*monster["health_range"]),
        "power": random.randint(*monster["power_range"]),
        "money": round(random.uniform(*monster["money_range"]), 2),
    }

def print_welcome(name: str):
    """
    Displays a welcome message for the player.
    Parameters:
        The player's name.
    """
    
    print(f"{'Hello, ' + name + '!':^20}")

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """
    Displays a shop item with two items with the items prices.
    
     Parameters:
        item1Name: Name of the first item.
        item1Price: Price of the first item.
        item2Name: Name of the second item.
        item2Price: Price of the second item.

    """
    print("+" + "-" * 22 + "+")
    print(f"| {item1Name:<12}${item1Price:>6.2f} |")
    print(f"| {item2Name:<12}${item2Price:>6.2f} |")
    print("+" + "-" * 22 + "+")


def test_functions():
    """ Test all the functions with an output.
        The output is displayed for the user"""

    # Print names
    names = ["Ash", "Misty", "Brock"]
    for name in names:
        print_welcome(name)
    
    # Print shop menu
    shop_items = [
        ("Pokeball", 25.00, "Greatball", 50.00),
        ("RazzBerry", 15.00, "NanabBerry", 25.00),
        ("Antidote", 20.00, "Awakening", 25.00)
    ]
    for items in shop_items:
        print_shop_menu(*items)

    # Pokemon Generator
    for _ in range(3):
        my_monster = new_random_monster()
        print("\nMonster Generated:")
        for key, value in my_monster.items():
            print(f"{key}: {value}")
        
    # Test Puchase_item    
    items_bought, remaining_cash = purchase_item(30.0, 100.0, 3)
    print(f"\nPurchased {items_bought} items, remaining money: ${remaining_cash}")

if __name__ == "__main__":
    test_functions()
