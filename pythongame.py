from gamefunctions import new_random_monster
import random

def main():
    hp, money = 500, 100
    while hp > 0:
        print(f"\nHP: {hp}, Money: {money}\n1) Fight\n2) Sleep (-5 Money)\n3) Quit")
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
        elif choice in ['3', 'quit']:
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



