import pygame
import json
import os

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
FONT_SIZE = 30
JSON_FILE = "Database/homework_data.json"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 122, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Homework Manager")
font = pygame.font.Font(None, FONT_SIZE)

# Load or initialize homework data
if os.path.exists(JSON_FILE):
    with open(JSON_FILE, "r") as file:
        homework_data = json.load(file)
else:
    homework_data = {"homeworks": []}

def save_homework_data():
    with open(JSON_FILE, "w") as file:
        json.dump(homework_data, file, indent=4)

def draw_text(surface, text, position, color=BLACK):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def main():
    running = True
    button_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT - BUTTON_HEIGHT - 20, BUTTON_WIDTH, BUTTON_HEIGHT)

    while running:
        screen.fill(WHITE)

        # Display homework
        y_offset = 20
        draw_text(screen, "Homework List:", (20, y_offset))
        for i, hw in enumerate(homework_data["homeworks"]):
            y_offset += FONT_SIZE + 10
            draw_text(screen, f"{i + 1}. {hw}", (20, y_offset))

        # Draw button
        pygame.draw.rect(screen, BLUE, button_rect)
        draw_text(screen, "Add Homework", button_rect.center, WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    # Add homework logic
                    new_hw = input("Enter new homework: ")
                    homework_data["homeworks"].append(new_hw)
                    save_homework_data()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
