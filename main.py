import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock() # Use to calculate tick for fps
    dt = 0 # Delta Time, used to convert ms to s
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt) # Update player rotation
        screen.fill("black") # Draw a black background
        player.draw(screen) # Draw the player on the screen
        pygame.display.flip() # Refresh the screen
        dt = clock.tick(60) / 1000 # Calculate the dt

if __name__ == "__main__":
    main()