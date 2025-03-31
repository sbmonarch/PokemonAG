from gamefunctions import new_random_monster, save_game, load_game
import random

def main():
    hp, money = 500, 100
    inventory = {}

    print("1) Start New Game\n2) Load Game")
    choice = input("Select an option: ").strip()

    if choice == "2":
        filename = input("Enter save file name: ").strip()
        inventory, money = load_game(filename)

    while hp > 0:
        print(f"\nHP: {hp}, Money: {money}\n1) Fight\n2) Sleep (-5 Money)\n3) Save & Quit\n4) Quit")
        choice = input("Action: ").strip().lower()
        
        if choice in ['1', 'fight']:
            monster = new_random_monster()
            print(f"You encounter {monster['name']}!")
            hp, money = fight(hp, money, monster)
        elif choice in ['2', 'sleep']:
            if money >= 5:
                hp += 10
                money -= 5
                print("You feel refreshed.")
            else:
                print("Not enough money!")
        elif choice in ['3', 'save & quit']:
            filename = input("Enter save file name: ").strip()
            save_game(filename, inventory, money)
            print("Game saved. Goodbye!")
            break
        elif choice in ['4', 'quit']:
            print("Game over!")
            break
        else:
            print("Invalid input. Try again.")

        if hp <= 0:
            print("You have fainted. Game over.")

def fight(hp, money, monster):
    while hp > 0 and monster['health'] > 0:
        action = input("1) Attack  2) Run: ").strip().lower()
        if action in ['1', 'attack']:
            player_damage = random.randint(50, 99)
            monster_damage = random.randint(50, 99)
            monster['health'] -= player_damage
            hp -= monster_damage
            print(f"Dealt {player_damage}, took {monster_damage}.")
        elif action in ['2', 'run']:
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




