import pygame

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self._update_text()
        self.position = self.text.get_rect()
        self.position.topleft = (10, 10)

    def _update_text(self):
        self.text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
    
    def add_points(self, points):
        self.score += points
        self._update_text()
    
    def draw(self, screen):
        screen.blit(self.text, self.position)