import pygame
import sys
from ui import UI, NameInputScreen, PreLevelScreen, DeathScreen, GameOverScreen, WinScreen  # Ensure all necessary imports
from level import Level
from astronaut import Player
from camera import Camera
from part import Part

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Your Game Title")
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_level = 1
        self.ui = UI(self.screen)
        self.player = None
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.level = None
        self.name_input_screen = NameInputScreen(self.screen)
        self.pre_level_screen = None

    def run(self):
        self.show_name_input_screen()
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def show_name_input_screen(self):
        name = None
        while name is None:
            self.name_input_screen.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                name = self.name_input_screen.handle_event(event)

    def start_level(self):
        self.level = Level(self.current_level)
        self.player = Player(100, 100)
        self.platforms = pygame.sprite.Group(*self.level.platforms)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.player:
                self.player.update(self.platforms)

    def update(self):
        if self.player:
            delta_time = self.clock.get_time() / 1000.0  # Convert milliseconds to seconds
            self.level.update_oxygen(delta_time)
            if self.level.is_complete():
                self.current_level += 1
                if self.current_level > 5:  # Assume there are 5 levels
                    self.running = False  # End the game or go to the win screen
                else:
                    self.start_level()

    def draw(self):
        # Draw background
        self.screen.fill((0, 0, 0))  # Clear screen with black
        if self.level and self.level.background:
            self.screen.blit(self.level.background, (0, 0))

        # Draw platforms
        self.platforms.draw(self.screen)

        # Update camera and draw player
        camera_position = self.camera.apply(self.player)
        self.camera.update(self.player)

        # Draw the player
        self.screen.blit(self.player.image, camera_position)

        # Draw UI
        self.ui.draw_oxygen_bar(self.level.current_oxygen / self.level.max_oxygen)
        self.ui.display_collected_parts(self.level.collected_parts, self.level.parts_required)

        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.start_level()  # Start the first level
    game.run()
