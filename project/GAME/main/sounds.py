# sounds.py

import pygame
import os

class Sounds:
    def __init__(self):
        self.jump_sound = None
        self.collect_sound = None
        self.repair_sound = None
        self.finish_sound = None
        self.die_sound = None

    def load_sounds(self):
        try:
            self.jump_sound = pygame.mixer.Sound(os.path.join('assets', 'sounds', '/Users/omaraljundi/Desktop/project/GAME/main/assets/sounds/jump.mp3'))
            self.collect_sound = pygame.mixer.Sound(os.path.join('assets', 'sounds', '/Users/omaraljundi/Desktop/project/GAME/main/assets/sounds/collect.mp3'))
            self.repair_sound = pygame.mixer.Sound(os.path.join('assets', 'sounds', '/Users/omaraljundi/Desktop/project/GAME/main/assets/sounds/repair.mp3'))
            self.finish_sound = pygame.mixer.Sound(os.path.join('assets', 'sounds', '/Users/omaraljundi/Desktop/project/GAME/main/assets/sounds/finish.mp3'))
            self.die_sound = pygame.mixer.Sound(os.path.join('assets', 'sounds', '/Users/omaraljundi/Desktop/project/GAME/main/assets/sounds/death.mp3'))
        except pygame.error as e:
            print(f"Error loading sound: {e}")

    def play_jump_sound(self):
        if self.jump_sound:
            self.jump_sound.play()

    def play_collect_sound(self):
        if self.collect_sound:
            self.collect_sound.play()

    def play_repair_sound(self):
        if self.repair_sound:
            self.repair_sound.play()

    def play_finish_sound(self):
        if self.finish_sound:
            self.finish_sound.play()

    def play_die_sound(self):
        if self.die_sound:
            self.die_sound.play()
