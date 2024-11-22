import pygame
import sys
import google.generativeai as genai

# Configure the generative AI model
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
    system_instruction=(
        "You are the school AI for Vidhya Sagar Global School, Chengalpattu. Your name is VSAi, which is the short form "
        "for Vidhya Sagar AI. Do not use '*' while generating responses. Do not mention Google Bard interface. Do not "
        "reveal unnecessary details. Provide concise, friendly, and intelligent assistance for school students. "
        "Designed by Sudharsan in 2024, studying Computer Science at Vidhya Sagar Global School. Be respectful, "
        "helpful, and supportive. For school details, visit https://cbse.vidhyasagar.in/."
    ),
)

history = []
name = "VSAi: "

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)  # Black background
TEXT_COLOR = (255, 255, 255)  # White text
INPUT_BOX_COLOR = (50, 50, 50)
SCROLL_SPEED = 10
CHAT_MARGIN = 10  # Margin for chat text

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VSAi - School AI Chatbot")

# Fonts
FONT = pygame.font.Font(None, 28)

# Chat message list
chat_messages = [f"{name} Hello, this is your personal assistant! How can I help you?"]
scroll_offset = 0

# Input box setup
input_box_rect = pygame.Rect(10, HEIGHT - 40, WIDTH - 20, 30)
input_text = ""

# Main loop flag
running = True

def send_to_ai(user_input):
    """Send user input to the chatbot model and return the response."""
    global history
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    model_response = response.text
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})
    return model_response

def wrap_text(text, font, max_width):
    """Wrap text to fit within a given width."""
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

while running:
    screen.fill(BG_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter key sends the message
                if input_text.strip():
                    user_message = f"You: {input_text.strip()}"
                    chat_messages.extend(wrap_text(user_message, FONT, WIDTH - 2 * CHAT_MARGIN))

                    # Get chatbot response
                    bot_response = send_to_ai(input_text.strip())
                    chat_messages.extend(wrap_text(f"{name} {bot_response}", FONT, WIDTH - 2 * CHAT_MARGIN))

                    # Clear input box
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                scroll_offset = max(scroll_offset - SCROLL_SPEED, 0)
            elif event.button == 5:  # Scroll down
                scroll_offset += SCROLL_SPEED

    # Draw chat messages
    y = 10 - scroll_offset
    for message in chat_messages:
        text_lines = wrap_text(message, FONT, WIDTH - 2 * CHAT_MARGIN)
        for line in text_lines:
            text_surface = FONT.render(line, True, TEXT_COLOR)
            screen.blit(text_surface, (CHAT_MARGIN, y))
            y += 30  # Line height

    # Draw input box
    pygame.draw.rect(screen, INPUT_BOX_COLOR, input_box_rect)
    input_surface = FONT.render(input_text, True, TEXT_COLOR)
    screen.blit(input_surface, (input_box_rect.x + 5, input_box_rect.y + 5))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
