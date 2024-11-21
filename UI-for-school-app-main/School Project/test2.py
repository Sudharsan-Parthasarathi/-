import pygame

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Scroll to Move Rectangle')

# Define rectangle properties
rect_width, rect_height = 50, 50
rect_x = (width - rect_width) // 2
rect_y = (height - rect_height) // 2
rect_speed = 10  # Speed of movement

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill screen with black
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                rect_y -= rect_speed
            elif event.button == 5:  # Scroll down
                rect_y += rect_speed

    # Ensure rectangle stays within screen boundaries
    if rect_y < 0:
        rect_y = 0
    elif rect_y > height - rect_height:
        rect_y = height - rect_height

    # Draw the rectangle
    pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))
    
    pygame.display.flip()  # Update the display
    pygame.time.Clock().tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()

