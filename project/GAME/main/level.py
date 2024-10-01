import pygame
from platformm import Platform
from part import Part

class Level:
    def __init__(self, level_number):
        if level_number is None:
            raise ValueError("Level number cannot be null")
        
        self.level_number = level_number
        self.planet_name, self.real_gravity = self.get_planet_info(level_number)
        self.platforms = self.create_platforms()
        self.parts = Part.generate_parts(10, [p.rect for p in self.platforms])
        self.gameplay_gravity = self.set_gravity()

        self.collected_parts = {
            'Power Cores': 0,
            'Metal Plates': 0,
            'Cooling Tubes': 0,
            'Fuel Rods': 0,
            'Wiring Kits': 0,
        }

        self.parts_required = {
            'Power Cores': 2,
            'Metal Plates': 2,
            'Cooling Tubes': 2,
            'Fuel Rods': 2,  # Fixed spelling
            'Wiring Kits': 2,
        }
        
        self.level_width = max([platform.rect.right for platform in self.platforms])
        self.level_height = max([platform.rect.bottom for platform in self.platforms])
        
        self.max_oxygen = 100
        self.current_oxygen = self.max_oxygen
        self.oxygen_depletion_rate = self.calculate_oxygen_depletion_rate()
        self.background = self.load_background()

    def load_background(self):
        backgrounds = {
            1: '/Users/omaraljundi/Desktop/project/GAME/Jupiter/Background.png',
            2: '/Users/omaraljundi/Desktop/project/GAME/Venus/Background.png',
            3: '/Users/omaraljundi/Desktop/project/GAME/Mars/Background.png',
            4: '/Users/omaraljundi/Desktop/project/GAME/Mercury/Background.png',
            5: '/Users/omaraljundi/Desktop/project/GAME/Moon/Background.png',
        }
        return pygame.image.load(backgrounds.get(self.level_number, ''))

    def get_planet_info(self, level_number):
        planets = {
            1: ("Jupiter", 24.79),
            2: ("Venus", 8.87),
            3: ("Mars", 3.71),
            4: ("Mercury", 3.7),
            5: ("The Moon", 1.62),
        }
        return planets.get(level_number, ("Unknown", 9.8))

    def create_platforms(self):
        platforms = []
        if self.level_number == 1:
            platforms.append(Platform(50, 500, 200, 20))
            platforms.append(Platform(300, 400, 200, 20))
            platforms.append(Platform(600, 300, 200, 20))
        elif self.level_number == 2:
            platforms.append(Platform(100, 450, 200, 20))
            platforms.append(Platform(350, 350, 200, 20))
            platforms.append(Platform(550, 250, 200, 20))
        # Add more platform setups for other levels...
        return platforms

    def set_gravity(self):
        gravity_levels = {
            1: 1.5,
            2: 1.2,
            3: 1.0,
            4: 0.8,
            5: 0.5,
        }
        return gravity_levels.get(self.level_number, 1.0)

    def calculate_oxygen_depletion_rate(self):
        total_time = 180
        return self.max_oxygen / total_time

    def update_oxygen(self, delta_time):
        if self.current_oxygen <= 0:
            self.game_over()
        else:
            self.current_oxygen -= self.oxygen_depletion_rate * delta_time

    def is_complete(self):
        return all(count >= self.parts_required[part] for part, count in self.collected_parts.items())

    def game_over(self):
        print("Game Over! Oxygen depleted.")
