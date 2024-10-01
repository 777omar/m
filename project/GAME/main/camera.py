import pygame 

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def apply_background(self):
        return self.camera.topleft

    def update(self, target):
        # Center the camera on the target
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)
        
        # Keep the camera within the bounds of the level
        x = min(0, x)  # Prevent scrolling past the left side
        x = max(-(self.width - self.camera.width), x)  # Prevent scrolling past the right side
        y = min(0, y)  # Prevent scrolling past the top
        y = max(-(self.height - self.camera.height), y)  # Prevent scrolling past the bottom
        
        self.camera = pygame.Rect(x, y, self.width, self.height)
