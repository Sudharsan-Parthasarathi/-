import pygame
import google.generativeai as genai

# Configuring the chatbot
genai.configure(api_key="AIzaSyBC2tKHZFF3y_8YxhxPIp51KgT8j_Z-Ayg")

generation_config = {
    "temperature": 1.5,
    "top_p": 1,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="you are the school AI for Vidhya Sagar Global School, Chengalpattu. Your name is VSAi...",
)

history = []

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VSAi Chatbot")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 128, 0)  # Color for user text
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 28)  # Slightly larger font for spaciousness

# UI Components
input_box = pygame.Rect(20, HEIGHT - 50, WIDTH - 40, 40)
scrollable_area = pygame.Rect(20, 20, WIDTH - 40, HEIGHT - 80)

# Variables
chat_lines = [("VSAi: Hi, I'm your personal AI assistant, how can I help you?", False)]  # Initial greeting
user_input = ""
scroll_offset = 0

SPACING = 20  # Space between messages


def wrap_text(text, font, max_width):
    """Wraps text to fit within a specified width."""
    lines = []
    words = text.split(" ")
    line = ""
    for word in words:
        test_line = f"{line} {word}".strip()
        if font.size(test_line)[0] > max_width:
            lines.append(line.strip())
            line = word
        else:
            line = test_line
    lines.append(line.strip())
    return lines


def render_chat(surface, chat_lines, scroll_offset):
    """Renders the chat lines to the scrollable area."""
    y = scrollable_area.top - scroll_offset
    for line, is_user in chat_lines:
        color = DARK_GREEN if is_user else WHITE
        for wrapped_line in wrap_text(line, font, scrollable_area.width):
            if y + font.get_height() > scrollable_area.top:
                text_surface = font.render(wrapped_line, True, color)
                surface.blit(text_surface, (scrollable_area.left, y))
            y += font.get_height()
        y += SPACING
        if y > scrollable_area.bottom:
            break


def chatbot_response(user_input):
    """Gets a response from the chatbot."""
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [response.text]})
    return response.text


running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_input.strip():
                    chat_lines.append((f"You: {user_input}", True))
                    bot_response = chatbot_response(user_input)
                    chat_lines.append((f"VSAi: {bot_response}", False))
                    user_input = ""
                    scroll_offset = max(0, len(chat_lines) * (font.get_height() + SPACING) - scrollable_area.height)
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                scroll_offset = max(scroll_offset - 20, 0)
            elif event.button == 5:  # Scroll down
                scroll_offset = min(scroll_offset + 20, len(chat_lines) * (font.get_height() + SPACING) - scrollable_area.height)

    # Render Chat Area
    render_chat(screen, chat_lines, scroll_offset)

    # Render Input Box
    pygame.draw.rect(screen, GRAY, input_box, border_radius=10)
    text_surface = font.render(user_input, True, BLACK)
    screen.blit(text_surface, (input_box.x + 10, input_box.y + 8))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
