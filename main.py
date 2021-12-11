# Import modules
import pygame

# Set window display constants
window = None
resolution = (1280, 720)
title = "PyGameEngine"

# Set frame timing constants
fps = 144
clock = None

# Main game function
def main():

    # Set window resolution & title
    window = pygame.display.set_mode(resolution)
    pygame.display.set_caption(title)

    # Initialize game clock
    clock = pygame.time.Clock()
    
    # Game loop
    run = True
    while run:
        clock.tick(fps)

        # Event loop
        for event in pygame.event.get():

            # Quit even
            if event.type = pygame.QUIT:
                run = False
        
# Only run game when exectuted directly
if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()