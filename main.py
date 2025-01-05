import pygame
from circleshape import *
from player import *
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    fill_and_display(player)

    
def fill_and_display(player):
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == pygame.QUIT:  # Check for quit event
                return  # Exit the loop and end the function
        screen.fill(black)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()