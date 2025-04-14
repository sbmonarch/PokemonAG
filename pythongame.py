import random
from gamefunctions import (
    new_random_monster,
    save_game,
    load_game,
    use_auto_defeat_item,
    equip_item,
    purchase_item,
    print_shop_menu,
    run_map
)

def main():
    hp, money = 500, 100
    inventory = []
    position = [0, 0]

    print("1) Start New Game\n2) Load Game")
    choice = input("Select an option: ").strip()

    if choice == "2":
        filename = input("Enter save file name: ").strip()
        inventory, money = load_game(filename)

    while hp > 0:
        print(f"\nHP: {hp}, Money: {money}")
        print("1) Fight\n2) Sleep (-5 Money)\n3) Equip Item\n4) Visit Shop\n5) Save & Quit\n6) Quit\n7) Visit Map")
        choice = input("Action: ").strip().lower()

        if choice in ['1', 'fight']:
            monster = new_random_monster()
            print(f"You encounter {monster['name']}!")
            hp, money = fight(hp, money, monster, inventory)
        elif choice in ['2', 'sleep']:
            if money >= 5:
                hp += 10
                money -= 5
                print("You feel refreshed.")
            else:
                print("Not enough money!")
        elif choice in ['3', 'equip item']:
            item_type = input("Equip a weapon or consumable: ").strip().lower()
            equipped_item = equip_item(inventory, item_type)
            if not equipped_item:
                print("No item equipped.")
        elif choice in ['4', 'shop', 'visit shop']:
            items = [
                ("Pokeball", 25.00, "Greatball", 50.00),
                ("Quick Claw Knife", 100.00, "Mewtwo Saber", 150.00),
                ("RazzBerry", 15.00, "NanabBerry", 25.00),
                ("Antidote", 20.00, "Awakening", 25.00)
            ]
            print_shop_menu(items)
            item = input("Buy Pokeball (1), Greatball (2), Quick Claw Knife (3), Mewtwo Saber (4), RazzBerry (5), NanabBerry (6), Antidote (7), Awakening (8)? ").strip()

            if item == "1":
                qty, money = purchase_item(25.00, money)
                if qty: inventory.append({"name": "Pokeball", "type": "misc"}); print("Pokeball added to inventory.")
            elif item == "2":
                qty, money = purchase_item(50.00, money)
                if qty: inventory.append({"name": "Greatball", "type": "misc"}); print("Greatball added to inventory.")
            elif item == "3":
                qty, money = purchase_item(100.00, money)
                if qty: inventory.append({"name": "Quick Claw Knife", "type": "weapon", "maxDurability": 15, "currentDurability": 15}); print("Quick Claw Knife added to inventory.")
            elif item == "4":
                qty, money = purchase_item(150.00, money)
                if qty: inventory.append({"name": "Mewtwo Saber", "type": "consumable", "effect": "auto-defeat"}); print("Mewtwo Saber added to inventory.")
            elif item == "5":
                qty, money = purchase_item(15.00, money)
                if qty: inventory.append({"name": "RazzBerry", "type": "consumable"}); print("RazzBerry added to inventory.")
            elif item == "6":
                qty, money = purchase_item(25.00, money)
                if qty: inventory.append({"name": "NanabBerry", "type": "consumable"}); print("NanabBerry added to inventory.")
            elif item == "7":
                qty, money = purchase_item(20.00, money)
                if qty: inventory.append({"name": "Antidote", "type": "consumable"}); print("Antidote added to inventory.")
            elif item == "8":
                qty, money = purchase_item(25.00, money)
                if qty: inventory.append({"name": "Awakening", "type": "consumable"}); print("Awakening added to inventory.")
            else:
                print("No purchase made.")
        elif choice in ['5', 'save', 'save & quit']:
            filename = input("Enter save file name: ").strip()
            save_game(filename, inventory, money)
            print("Game saved. Goodbye!")
            break
        elif choice in ['6', 'quit']:
            print("Game over!")
            break
        elif choice in ['7', 'map', 'visit map']:
            print("Visiting map...")
            encounter = run_map(position)  
            if encounter == "pokemon":
                print("A Pokémon encounter occurred!")
            elif encounter == "town":
                print("You visited the town.")  
            else:
                print("Invalid input. Try again.")

        if hp <= 0:
            print("You have fainted. Game over.")

def fight(hp, money, monster, inventory):
    while hp > 0 and monster['health'] > 0:
        action = input("1) Attack  2) Run: ").strip().lower()
        if action == "1":
            if use_auto_defeat_item(inventory):
                print("You instantly defeat the monster with an item!")
                money += monster['money']
                break
            else:
                player_damage = random.randint(50, 99)
                monster_damage = random.randint(50, 99)
                monster['health'] -= player_damage
                hp -= monster_damage
                print(f"Dealt {player_damage}, took {monster_damage}.")
        elif action == "2":
            print("You escaped!")
            break
        else:
            print("Invalid input. Try again.")

    if monster['health'] <= 0:
        money += monster['money']
        print(f"Defeated {monster['name']}. +{monster['money']} Money!")
    return hp, money

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()


