import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    fill_and_display()

    
def fill_and_display():
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == pygame.QUIT:  # Check for quit event
                return  # Exit the loop and end the function
        screen.fill(black)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()