#gamefunctions.py 
#Steven Bartoldus 
#April 13th

import random
import json
import pygame
from wanderingMonster import WanderingMonster, create_random_monsters

GRID_SIZE = 10
TILE_SIZE = 32
TOWN_POS = (0, 0)

def run_map(position, monsters=None):
    pygame.init()
    screen = pygame.display.set_mode((GRID_SIZE * TILE_SIZE, GRID_SIZE * TILE_SIZE))
    pygame.display.set_caption("Explore Kinto")

    x, y = position
    clock = pygame.time.Clock()
    running = True
    encounter = None
    
    if monsters is None:
        monsters = create_random_monsters()
    
    move_counter = 0

    while running:
        screen.fill((255, 255, 255))

        pygame.draw.circle(screen, (0, 255, 0), 
                         (TOWN_POS[0] * TILE_SIZE + 16, 
                          TOWN_POS[1] * TILE_SIZE + 16), 10)
        
        pygame.draw.rect(screen, (0, 0, 255), 
                        pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, 
                                   TILE_SIZE, TILE_SIZE))
        
        for monster in monsters:
            pygame.draw.circle(screen, monster.color,
                             (monster.position[0] * TILE_SIZE + 16,
                              monster.position[1] * TILE_SIZE + 16), 10)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                new_x, new_y = x, y
                if event.key == pygame.K_UP and y > 0:
                    new_y -= 1
                elif event.key == pygame.K_DOWN and y < GRID_SIZE - 1:
                    new_y += 1
                elif event.key == pygame.K_LEFT and x > 0:
                    new_x -= 1
                elif event.key == pygame.K_RIGHT and x < GRID_SIZE - 1:
                    new_x += 1
                else:
                    continue
                
                for monster in monsters[:]:
                    if (new_x, new_y) == monster.position:
                        encounter = {"type": "monster", "monster": monster}
                        monsters.remove(monster)
                        running = False
                        break
                
                if not encounter:
                    x, y = new_x, new_y
                    move_counter += 1
                    
                    if move_counter % 2 == 0:
                        for monster in monsters:
                            monster.move()
                            
                            if (x, y) == monster.position:
                                encounter = {"type": "monster", "monster": monster}
                                monsters.remove(monster)
                                running = False
                                break

                if (x, y) == TOWN_POS:
                    encounter = {"type": "town"}
                    running = False

        clock.tick(10)

    position[0], position[1] = x, y
    pygame.quit()
    return encounter, monsters

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    max_affordable = int(startingMoney // itemPrice)
    quantity_purchased = min(quantityToPurchase, max_affordable)
    remaining_money = round(startingMoney - (quantity_purchased * itemPrice), 2)
    return quantity_purchased, remaining_money

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

def use_auto_defeat_item(inventory):
    for item in inventory:
        if item.get("type") == "consumable" and item.get("effect") == "auto-defeat":
            inventory.remove(item)
            print("The Mewtwo Saber activates and defeats the monster!")
            return True
    return False

def print_welcome(name):
    print(f"{'Hello, ' + name + '!':^20}")

def print_shop_menu(items):
    print("+" + "-" * 22 + "+")
    for item1, price1, item2, price2 in items:
        print(f"| {item1:<15} ${price1:>6.2f} | {item2:<15} ${price2:>6.2f} |")
    print("+" + "-" * 22 + "+")

def save_game(filename, inventory, money, monsters=None):
    data = {
        "inventory": inventory,
        "money": money,
        "monsters": [m.to_dict() for m in monsters] if monsters else []
    }
    with open(filename, 'w') as file:
        json.dump(data, file)
    print("Game saved successfully.")

def load_game(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        
        monsters = [WanderingMonster.from_dict(m) for m in data.get("monsters", [])]
        return data.get("inventory", []), data.get("money", 0.0), monsters
    except (FileNotFoundError, json.JSONDecodeError):
        print("Failed to load game. Starting a new game.")
        return [], 0.0, []
