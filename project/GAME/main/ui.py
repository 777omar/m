import pygame

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('/Users/omaraljundi/Downloads/elegant_4/Elegant DEMO.ttf', 24)  # Adjust path as needed
        self.oxygen_image = pygame.image.load('/Users/omaraljundi/Desktop/project/GAME/main/assets/oxygen.png').convert_alpha()  # Adjust path as needed

    def draw_oxygen_bar(self, oxygen_percentage):
        oxygen_width = int(self.oxygen_image.get_width() * oxygen_percentage)
        # Draw the oxygen bar
        self.screen.blit(self.oxygen_image, (10, 10))  # Draw background
        pygame.draw.rect(self.screen, (0, 255, 0), (10, 10, oxygen_width, self.oxygen_image.get_height()))  # Draw foreground

    def display_collected_parts(self, collected_parts, parts_required):
        # Display collected parts on the screen
        y_offset = 40
        for part, required in parts_required.items():
            collected = collected_parts.get(part, 0)
            text = f"{part}: {collected}/{required}"
            text_surface = self.font.render(text, True, (255, 255, 255))
            self.screen.blit(text_surface, (10, y_offset))
            y_offset += 30

class NameInputScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('/Users/omaraljundi/Downloads/elegant_4/Elegant DEMO.ttf', 24)  # Adjust path as needed
        self.input_text = ""
        self.active = True

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Confirm name input
                self.active = False
                return self.input_text
            elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                self.input_text = self.input_text[:-1]
            else:  # Append any other character
                self.input_text += event.unicode

        return None

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen
        input_surface = self.font.render(self.input_text, True, (255, 255, 255))  # Render input text
        self.screen.blit(input_surface, (100, 100))  # Display text at position
        pygame.display.flip()  # Update the display

class PreLevelScreen:
    def __init__(self, screen, level_number):
        self.screen = screen
        self.font = pygame.font.Font('/Users/omaraljundi/Downloads/elegant_4/Elegant DEMO.ttf', 24)  # Adjust path as needed
        self.level_number = level_number

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen
        title_surface = self.font.render(f"Welcome to Level {self.level_number}", True, (255, 255, 255))
        self.screen.blit(title_surface, (100, 100))
        instruction_surface = self.font.render("Press Enter to start!", True, (255, 255, 255))
        self.screen.blit(instruction_surface, (100, 150))
        pygame.display.flip()

class DeathScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('/Users/omaraljundi/Downloads/elegant_4/Elegant DEMO.ttf', 24)  # Adjust path as needed

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen
        death_surface = self.font.render("You Died!", True, (255, 0, 0))
        self.screen.blit(death_surface, (100, 100))
        instruction_surface = self.font.render("Press Enter to restart!", True, (255, 255, 255))
        self.screen.blit(instruction_surface, (100, 150))
        pygame.display.flip()

class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('/Users/omaraljundi/Downloads/elegant_4/Elegant DEMO.ttf', 24)  # Adjust path as needed

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen
        game_over_surface = self.font.render("Game Over!", True, (255, 0, 0))
        self.screen.blit(game_over_surface, (100, 100))
        instruction_surface = self.font.render("Press Enter to quit!", True, (255, 255, 255))
        self.screen.blit(instruction_surface, (100, 150))
        pygame.display.flip()

class WinScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('/Users/omaraljundi/Downloads/elegant_4/Elegant DEMO.ttf', 24)  # Adjust path as needed

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen
        win_surface = self.font.render("You Win!", True, (0, 255, 0))
        self.screen.blit(win_surface, (100, 100))
        instruction_surface = self.font.render("Press Enter to play again!", True, (255, 255, 255))
        self.screen.blit(instruction_surface, (100, 150))
        pygame.display.flip()
