import random
import pygame

class WanderingMonster:
    MONSTER_TYPES = [
        {"name": "Snorlax", "description": "A sleepy Pokemon blocking your path.", 
         "health_range": (220, 280), "power_range": (70, 110), 
         "money_range": (30, 130), "color": (139, 69, 19)},
        {"name": "Charizard", "description": "A dragon-like Pokemon with fire breath.", 
         "health_range": (150, 250), "power_range": (80, 120), 
         "money_range": (50, 150), "color": (255, 69, 0)},
        {"name": "Mewtwo", "description": "A powerful psychic Pokemon.", 
         "health_range": (200, 330), "power_range": (170, 220), 
         "money_range": (40, 170), "color": (148, 0, 211)}
    ]
    
    def __init__(self, grid_size=10, town_pos=(0, 0)):
        monster_type = random.choice(self.MONSTER_TYPES)
        self.name = monster_type["name"]
        self.description = monster_type["description"]
        self.health = random.randint(*monster_type["health_range"])
        self.power = random.randint(*monster_type["power_range"])
        self.money = round(random.uniform(*monster_type["money_range"]), 2)
        self.color = monster_type["color"]
        self.grid_size = grid_size
        self.town_pos = town_pos
        
        while True:
            self.position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
            if self.position != town_pos and self.position != (0, 0):
                break
    
    def move(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            new_x, new_y = self.position[0] + dx, self.position[1] + dy
            if (0 <= new_x < self.grid_size and 
                0 <= new_y < self.grid_size and 
                (new_x, new_y) != self.town_pos):
                self.position = (new_x, new_y)
                return True
        return False
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "health": self.health,
            "power": self.power,
            "money": self.money,
            "color": self.color,
            "position": self.position
        }
    
    @classmethod
    def from_dict(cls, data, grid_size=10, town_pos=(0, 0)):
        monster = cls.__new__(cls)
        monster.name = data["name"]
        monster.description = data["description"]
        monster.health = data["health"]
        monster.power = data["power"]
        monster.money = data["money"]
        monster.color = data["color"]
        monster.position = data["position"]
        monster.grid_size = grid_size
        monster.town_pos = town_pos
        return monster

def create_random_monsters(count=2, grid_size=10, town_pos=(0, 0)):
    monsters = []
    positions = {town_pos, (0, 0)}
    
    while len(monsters) < count:
        monster = WanderingMonster(grid_size, town_pos)
        if monster.position not in positions:
            monsters.append(monster)
            positions.add(monster.position)
    
    return monsters
