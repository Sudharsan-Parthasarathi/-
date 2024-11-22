import pygame
import pygame as pg
import os.path
import google.generativeai as genai
import random
import sys
from pygame.locals import *
import time
import json
import os
import math

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

pygame.init()

#All about the screen
info=pygame.display.Info()
winsize=(info.current_w,info.current_h)
screen=pygame.display.set_mode(winsize)
pygame.display.set_caption("School app...")
screen.fill((30,30,30))#main_Background

#Font for displaying text
font=pygame.font.Font('Assets/font.ttf',17)
font6=pygame.font.Font('Assets/font2.ttf',17)
font1=pygame.font.Font('Assets/font.ttf',35)
font2=pygame.font.Font('Assets/font.ttf',20)
font3=pygame.font.Font('Assets/font2.ttf',35)
font4=pygame.font.Font('Assets/font2.ttf',25)
font5=pygame.font.Font('Assets/font2.ttf',40)
font7=pygame.font.Font('Assets/font2.ttf',100)

#Animations
def option_state_animation_push():
    global left_rect_state
    left_rect_state+=5
    return left_rect_state
def option_state_animation_pull():
    global left_rect_state
    left_rect_state-=5
    return left_rect_state

#Colours
search_bar_colour=(90,90,90)
search_bar_border_colour=(150,150,150)
search_bar_text_colour=(180,180,180)
close_text_colour=(150,150,150)
_text_colour=(150,150,150)
_text2_colour=(150,150,150)

#Buttons
button_rect1=pygame.Rect(winsize[0]-370,4,300,22)
pygame.draw.rect(screen,(255,255,255),button_rect1,0,7)
button_rect2=pygame.Rect(winsize[0]-30,0,30,30)
pygame.draw.rect(screen,(70,70,70),button_rect2,0)
button_rect3=pygame.Rect(winsize[0]-60,0,30,30)
pygame.draw.rect(screen,(70,70,70),button_rect3,0)
button_rect4=pygame.Rect(0,0,30,30)
pygame.draw.rect(screen,(70,70,70),button_rect4,0)

#Search icon
search_icon=pygame.image.load('Assets/search_off.png')
search_icon_size=search_icon.get_size()
search_icon_newsize=(search_icon_size[0]//30,search_icon_size[1]//30)
search_icon_main=pygame.transform.smoothscale(search_icon,search_icon_newsize)
search_icon1=pygame.image.load('Assets/search_on.png')
search_icon_main1=pygame.transform.smoothscale(search_icon1,search_icon_newsize)

#button for option/icon
button_recta=pygame.Rect(0,32,50,50)
button_rectb=pygame.Rect(0,82,50,50)
button_rectc=pygame.Rect(0,132,50,50)
button_rectd=pygame.Rect(0,182,50,50)
button_recte=pygame.Rect(0,237,50,50)

#Buttons for login
button_rect_name=pygame.Rect(winsize[0]/2-132,winsize[1]/2-62,265,27)
button_rect_password=pygame.Rect(winsize[0]/2-133,winsize[1]/2+8,265,27)
login_button=pygame.Rect(winsize[0]/2-131.5,winsize[1]/2+93,220,70)

#Buttons for homework
text_add_rect=[winsize[0]-150,40,120,50]
text_add_rect1=[winsize[0]//2+230,winsize[0]//2+100,120,50]
text_rect=pygame.Rect(winsize[0]-150,40,120,50)
text_rect1=pygame.Rect(winsize[0]//2+230,winsize[0]//2+100,120,50)

#Images
school=pygame.image.load('Assets/school_off.png')
school_size=school.get_size()
school_newsize=(school_size[0]//15,school_size[1]//15)
school_main=pygame.transform.smoothscale(school,school_newsize)
school1=pygame.image.load('Assets/school_on.png')
school_main1=pygame.transform.smoothscale(school1,school_newsize)
school_xy=school_main.get_rect(center=button_recta.center)

ai=pygame.image.load('Assets/ai_off.png')
ai_size=ai.get_size()
ai_newsize=(ai_size[0]//15,ai_size[1]//15)
ai_main=pygame.transform.smoothscale(ai,ai_newsize)
ai1=pygame.image.load('Assets/ai_on.png')
ai_main1=pygame.transform.smoothscale(ai1,ai_newsize)
ai_xy=ai_main.get_rect(center=button_rectb.center)

pen=pygame.image.load('Assets/pen_off.png')
pen_size=pen.get_size()
pen_newsize=(pen_size[0]//15,pen_size[1]//15)
pen_main=pygame.transform.smoothscale(pen,pen_newsize)
pen1=pygame.image.load('Assets/pen_on.png')
pen_main1=pygame.transform.smoothscale(pen1,pen_newsize)
pen_xy=pen_main.get_rect(center=button_rectc.center)

game=pygame.image.load('Assets/game_off.png')
game_size=game.get_size()
game_newsize=(game_size[0]//15,game_size[1]//15)
game_main=pygame.transform.smoothscale(game,game_newsize)
game1=pygame.image.load('Assets/game_on.png')
game_main1=pygame.transform.smoothscale(game1,game_newsize)
game_xy=game_main.get_rect(center=button_rectd.center)

news=pygame.image.load('Assets/news_off.png')
news_size=news.get_size()
news_newsize=(news_size[0]//15,news_size[1]//15)
news_main=pygame.transform.smoothscale(news,news_newsize)
news1=pygame.image.load('Assets/news_on.png')
news_main1=pygame.transform.smoothscale(news1,news_newsize)
news_xy=news_main.get_rect(center=button_recte.center)

class school_op:
    def __init__(self,image_path_off,image_path_on):
        self.image=pygame.image.load(image_path_off)
        image_size=self.image.get_size()
        image_newsize=(image_size[0]//20,image_size[1]//20)
        self.main_image=pygame.transform.smoothscale(self.image,image_newsize)
        self.image1=pygame.image.load(image_path_on)
        self.main_image1=pygame.transform.smoothscale(self.image1,image_newsize)

    def draw(self,surface,x,y,state):
        if state=='on':
          surface.blit(self.main_image1,(x,y-3))
        else: surface.blit(self.main_image,(x,y))

images=[
    school_op('Assets/home_off.png','Assets/home_on.png'),
    #school_op('Assets/doc_off.png','Assets/doc_on.png'),
    school_op('Assets/att_off.png','Assets/att_on.png'),
    school_op('Assets/pro_off.png','Assets/pro_on.png'),
    school_op('Assets/exam_off.png','Assets/exam_on.png'),
    school_op('Assets/class_off.png','Assets/class_on.png')
]

profile=pygame.image.load('Assets/profile.png')
profile_size=news.get_size()
profile_newsize=(news_size[0]//3.3,news_size[1]//3.3)
profile_main=pygame.transform.smoothscale(profile,profile_newsize)

class school_bot2:
    def __init__(self,image_path_off,image_path_on):
        self.image=pygame.image.load(image_path_off)
        image_size=self.image.get_size()
        image_newsize=(image_size[0]//20,image_size[1]//20)
        self.main_image=pygame.transform.smoothscale(self.image,image_newsize)
        self.image1=pygame.image.load(image_path_on)
        self.main_image1=pygame.transform.smoothscale(self.image1,image_newsize)

    def draw(self,surface,x,y,state):
        if state=='on':
          surface.blit(self.main_image1,(x,y-3))
        else: surface.blit(self.main_image,(x,y))

images_bot2=[
    school_bot2('Assets/paint_off.png','Assets/paint_on.png'),
    school_bot2('Assets/era_off.png','Assets/era_on.png')
]

solve=pygame.image.load("Assets/solve_off.png")
solve_size=solve.get_size()
solve_newsize=(solve_size[0]//8.5,solve_size[1]//8.5)
main_solve=pygame.transform.smoothscale(solve,solve_newsize)
solve1=pygame.image.load("Assets/solve_on.png")
main_solve1=pygame.transform.smoothscale(solve1,solve_newsize)

#For cv
cv_colour=(255,255,255)
def draw_line(screen,start,end,width):
    pygame.draw.line(screen,cv_colour,start,end,width)

def save_image():
    timestamp=int(time.time())
    filename=f"saved_image/cv_image.png"
    pygame.image.save(subsurface,filename)
    return filename

#Json
def check_login(username, password):
 
    with open('Database/login.json', 'r') as file:
        users_data = json.load(file)

    for user in users_data["login"]:
        if user["name"] == username and user["password"] == password:
            print("Yes")
            return

    print("Incorrect password")

#For login
def load_users():
    try:
        with open('Database/login.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": []}
    
def check_login(username_input, password_input):
    users_data = load_users()
    for user in users_data["login"]:
        if user["name"] == username_input and user["password"] == password_input:
            return True
    return False

login=pygame.image.load("Assets/login.png")
login_size=login.get_size()
login_newsize=(login_size[0]//2.25,login_size[1]//2.15)
main_login=pygame.transform.smoothscale(login,login_newsize)

#For homework=====================================================================================================
JSON_FILE = "Database/homework_data.json"
if os.path.exists(JSON_FILE):
    with open(JSON_FILE, "r") as file:
        homework_data = json.load(file)
else:
    homework_data = {"homeworks": []}

JSON_FILE1 = "Database/class.json"
if os.path.exists(JSON_FILE1):
    with open(JSON_FILE1, "r") as file:
        class_data = json.load(file)

JSON_FILE2 = "Database/news.json"
if os.path.exists(JSON_FILE2):
    with open(JSON_FILE2, "r") as file:
        news_data = json.load(file)
        
add_text_1=""
line_height1 = 20
def render_text():
    lines1 = add_text_1.split('\n')
    rendered_lines = []

    for line1 in lines1:
        rendered_lines.append(font6.render(line1, True, (255,255,255)))

    return rendered_lines

def draw_multiline_text_with_rect(surface, text, start_pos, line_height, text_color=(255,255,255), rect_color=(70,70,70), padding=10):
    lines = text.split('\n')
    x, y = start_pos

    rect_height = (line_height * len(lines)) + padding * 2
    rect = pygame.Rect(x - padding, y - padding, winsize[0]-200-left_rect_state, rect_height)

    pygame.draw.rect(surface,rect_color,rect,0,15)
    pygame.draw.rect(surface,(120,120,120),rect,2,15)

    for line in lines:
        text_surface = font2.render(line, True, text_color)
        surface.blit(text_surface, (x, y))
        y += line_height  
    return rect_height + padding

def save_homework_data():
    with open(JSON_FILE, "w") as file:
        json.dump(homework_data, file, indent=4)
#next a
ABSENT_COLOR = (90,90,90)  # Red
PRESENT_COLOR = (50,50,50)  # Green
HOVER_COLOR = (200, 200, 200)
TOOLTIP_BG = (50, 50, 50)
TOOLTIP_TEXT = (255, 255, 255)

'''total_days = 30
absent_days = 2
present_days = total_days - absent_days'''

def get_present_by_name(name):
    global absent_angle,present_angle,absent_days,present_days,total_days
    users_data = load_users()
    for user in users_data["login"]:
        if user["name"] == name:
            day=user['present']
    total_days = 30
    present_days = day
    absent_days = total_days-present_days
    absent_angle = (absent_days / total_days) * 360
    present_angle = (present_days / total_days) * 360
    return absent_angle,present_angle,absent_days

CENTER = (winsize[0]// 2+130,winsize[1]// 2-40)
BASE_RADIUS = 150+50
HOVER_RADIUS = 170+50

def draw_segment(center, radius, start_angle, end_angle, color):
    points = [center]
    for angle in range(int(start_angle), int(end_angle) + 1):
        x = center[0] + radius * math.cos(math.radians(angle))
        y = center[1] + radius * math.sin(math.radians(angle))
        points.append((x, y))
    pygame.draw.polygon(screen, color, points)

def draw_pie_chart(hovered_segment=None):
    radius_absent = HOVER_RADIUS if hovered_segment == "absent" else BASE_RADIUS
    radius_present = HOVER_RADIUS if hovered_segment == "present" else BASE_RADIUS

    # Draw absent segment
    draw_segment(CENTER, radius_absent, 0, absent_angle, ABSENT_COLOR)
    # Draw present segment
    draw_segment(CENTER, radius_present, absent_angle, absent_angle + present_angle, PRESENT_COLOR)

def draw_labels():
    # Absent label
    absent_mid_angle = absent_angle / 2
    absent_x = CENTER[0] + (BASE_RADIUS + 50) * math.cos(math.radians(absent_mid_angle))
    absent_y = CENTER[1] + (BASE_RADIUS + 50) * math.sin(math.radians(absent_mid_angle))
    label = font.render(f"Absent: {absent_days} ({(absent_days / total_days) * 100:.1f}%)", True, (255,255,255))
    screen.blit(label, (absent_x - label.get_width() // 2, absent_y - label.get_height() // 2))

    # Present label
    present_mid_angle = absent_angle + (present_angle / 2)
    present_x = CENTER[0] + (BASE_RADIUS + 50) * math.cos(math.radians(present_mid_angle))
    present_y = CENTER[1] + (BASE_RADIUS + 50) * math.sin(math.radians(present_mid_angle))
    label = font.render(f"Present: {present_days} ({(present_days / total_days) * 100:.1f}%)", True, (255,255,255))
    screen.blit(label, (present_x - label.get_width() // 2, present_y - label.get_height() // 2))

def draw_legend():
    legend_x = CENTER[0] - 150
    legend_y = CENTER[1] + BASE_RADIUS + 50
    pygame.draw.rect(screen, (180,180,180), (legend_x, legend_y, 300, 80), border_radius=10)
    pygame.draw.rect(screen, (0,0,0), (legend_x, legend_y, 300, 80), 2, border_radius=10)

    # Legend labels
    pygame.draw.rect(screen, ABSENT_COLOR, (legend_x + 10, legend_y + 10, 20, 20))
    pygame.draw.rect(screen, PRESENT_COLOR, (legend_x + 10, legend_y + 50, 20, 20))
    absent_text = font.render(f"Absent: {absent_days} days", True, (0,0,0))
    present_text = font.render(f"Present: {present_days} days", True, (0,0,0))
    screen.blit(absent_text, (legend_x + 40, legend_y + 10))
    screen.blit(present_text, (legend_x + 40, legend_y + 50))

def draw_tooltip(mouse_pos, text):
    text_surface = font.render(text, True, TOOLTIP_TEXT)
    text_width, text_height = text_surface.get_width(), text_surface.get_height()
    pygame.draw.rect(screen, TOOLTIP_BG, (mouse_pos[0], mouse_pos[1], text_width + 10, text_height + 10), border_radius=5)
    screen.blit(text_surface, (mouse_pos[0] + 5, mouse_pos[1] + 5))

def check_hover(mouse_pos):
    dx, dy = mouse_pos[0] - CENTER[0], mouse_pos[1] - CENTER[1]
    distance = math.sqrt(dx**2 + dy**2)

    if distance <= BASE_RADIUS:
        angle = math.degrees(math.atan2(dy, dx))
        angle = (angle + 360) % 360

        if 0 <= angle < absent_angle:
            return "absent"
        elif absent_angle <= angle <= absent_angle + present_angle:
            return "present"
    return None

#next p
DARK_BG = (20, 20, 30)
WHITE = (255, 255, 255)
NEON_GREEN = (100,100,100)
NEON_BLUE = (70,70,70)
RED = (255, 69, 58)
GRID_COLOR = (50, 50, 70)
SHADOW = (10, 10, 15)

subjects = ["Maths", "CS", "Physics", "Chemistry", "English"]
#marks = [75, 90, 80, 85, 70] 
one=True
def get_marks(name):
  global one,marks,current_bar_lengths
  if one==True:
    users_data = load_users()
    for user in users_data["login"]:
        if user["name"] == name:
            marks=user['marks']
            return marks
    one=False

max_mark = 100

bar_width = 50
gap = 30
top_margin = 250
left_margin = 500
graph_width = 700
graph_height = len(subjects) * (bar_width + gap) - gap

animation_speed = 15  

#next e
test=pygame.image.load('Assets/test.png')
test_size=test.get_size()
test_cut=1.1
test_newsize=(test_size[0]//test_cut,test_size[1]//test_cut)
test_main=pygame.transform.smoothscale(test,test_newsize)

#ai
font = pygame.font.Font(None, 28)  # Slightly larger font for spaciousness

# UI Components
input_box = pygame.Rect(300, winsize[1] - 100, winsize[0] - 370, 40)
scrollable_area = pygame.Rect(300,60,winsize[0] - 370,winsize[1]-200)

chat_lines = [("VSAi: Hi, I'm your personal AI assistant, how can I help you?", False)]  # Initial greeting
user_input = ""
scroll_offset = 0

SPACING = 20 

def wrap_text(text, font, max_width):
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
    y = scrollable_area.top - scroll_offset
    for line, is_user in chat_lines:
        color = (200,200,200) if is_user else WHITE
        for wrapped_line in wrap_text(line, font, scrollable_area.width):
            if y + font.get_height() > scrollable_area.top:
                text_surface = font.render(wrapped_line, True, color)
                surface.blit(text_surface, (scrollable_area.left+10, y+10))
            y += font.get_height()
        y += SPACING
        if y > scrollable_area.bottom:
            break


def chatbot_response(user_input):
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [response.text]})
    return response.text

#Colours for button
coloura=(70,70,70)
colourb=(70,70,70)
colourc=(70,70,70)
colourd=(70,70,70)
coloure=(70,70,70)

colour1=(140,140,140)
colour2=(140,140,140)
colour3=(140,140,140)
colour4=(140,140,140)
colour5=(140,140,140)
colour6=(140,140,140)

solve_colour=(70,70,70)
solve_border_colour=(140,140,140)
solve_text_colour=(140,140,140)
box_colour=(50,50,50)
box_outter_colour=(140,140,140)

login_name_colour=(150,150,150)
login_password_colour=(150,150,150)
login_colour=(80,80,80)

add_colour=(200,200,200)
add_text_colour=(140,140,140)
add_colour1=(200,200,200)
add_text_colour1=(140,140,140)

#Variables
search_icon_state=0
option_state=1
left_rect_state=55
left2_rect_state=180
school_state=0
ai_state=0
pen_state=0
game_state=0
news_state=0
ss=ais=ps=gs=ns=0
sss=1
aiss=pss=gss=nss=0
squarey=32
text="School"
text_school="home_w"
state1=state2=state3=state4='off'
state5=state6='off'
state13=state23=state33=state43='off'
state53=state63='off'
school_store_xy1=school_store_xy2=school_store_xy3=(0,0)
school_store_xy4=school_store_xy5=school_store_xy6=(0,0)
h=1
c=a=p=e=s=0
tem_x,x=0,0
solve_on=False
drawing=False
last_pos=None
radius=15
username = ""
password = ""
username_active = False
password_active = False
dis_name=False
dis_pass=False
i_pass=False
FONT_SIZE=20
add_text_op=False
recover=1
two=True
rect_y,rect_y1,rect_y2=0,0,0
rect_speed=30

login_run=False
run=True
while run:
    if login_run:
      for event in pygame.event.get():

        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_ESCAPE:
              run=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            if button_rect2.collidepoint(event.pos):
                run=False
            if button_rect3.collidepoint(event.pos):
                pygame.display.iconify()

        if event.type==pygame.MOUSEMOTION:
            if button_rect2.collidepoint(event.pos):
                close_text_colour=(255,255,255)
            else:
                close_text_colour=(150,150,150)
            if button_rect3.collidepoint(event.pos):
                _text_colour=(255,255,255)
            else:
                _text_colour=(150,150,150)

            if button_rect_name.collidepoint(event.pos):
                login_name_colour=(255,255,255)
            else:
                login_name_colour=(150,150,150)
            if button_rect_password.collidepoint(event.pos):
                login_password_colour=(255,255,255)
            else:
                login_password_colour=(150,150,150)
            if login_button.collidepoint(event.pos):
                x=-3
                login_colour=(255,255,255)
            else:
                login_colour=(150,150,150)
                x=0

        if event.type == pygame.KEYDOWN:
            if username_active:
                i_pass=False
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
            elif password_active:
                i_pass=False
                if event.key == pygame.K_BACKSPACE:
                    password = password[:-1]
                else:
                    password += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect_name.collidepoint(event.pos):
                dis_name=True
                username_active = True
                password_active = False
            elif button_rect_password.collidepoint(event.pos):
                dis_pass=True
                password_active = True
                username_active = False
            else:
                username_active = False
                password_active = False

      screen.fill((60,60,60))

      #Close and - button
      close_text=font.render("X",True,close_text_colour)
      close_text_xy=close_text.get_rect(center=button_rect2.center)
      screen.blit(close_text,close_text_xy)
      _text=font1.render("-",True,_text_colour)
      _text_xy=_text.get_rect(center=button_rect3.center)
      screen.blit(_text,(_text_xy[0],_text_xy[1]-1))

      #Main login
      loginx=winsize[0]/2-login_newsize[0]/1.825
      loginy=winsize[1]/2-login_newsize[1]/2
      screen.blit(main_login,(loginx,loginy))

      #Render Text 
      name_text=font4.render("Name",True,login_name_colour)
      name_text_xy=name_text.get_rect(center=button_rect_name.center)
      screen.blit(name_text,(name_text_xy[0]-95,name_text_xy[1]))

      pass_text=font4.render("Password",True,login_password_colour)
      pass_text_xy=pass_text.get_rect(center=button_rect_password.center)
      screen.blit(pass_text,(pass_text_xy[0]-70,pass_text_xy[1]))

      match_colour=(58,58,58)
      if dis_name:
          pygame.draw.rect(screen,match_colour,button_rect_name)
      if dis_pass:
          pygame.draw.rect(screen,match_colour,button_rect_password)

      username_text = font4.render(username, True, (255,255,255))
      password_text = font4.render("*" * len(password), True, (255,255,255))
      screen.blit(username_text, (name_text_xy[0]-95,name_text_xy[1]))
      screen.blit(password_text, (pass_text_xy[0]-70,pass_text_xy[1]))

      login_text = font5.render("login", True, login_colour)
      login_text_xy=login_text.get_rect(center=login_button.center)
      screen.blit(login_text,(login_text_xy[0],login_text_xy[1]+x))

      if login_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        if check_login(username, password):
            login_run=False
            password = ""
        else:
            i_pass=True

      if i_pass:
            text1 = font2.render("Incorrect Password/User Name", True, (255,0,0))
            screen.blit(text1,(winsize[0]/2-155,winsize[1]/2-270))

      pygame.display.update()

    else:
      mouse_pos = pygame.mouse.get_pos()
      for event in pygame.event.get():

        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_ESCAPE:
              run=False
 
        if event.type==pygame.MOUSEBUTTONDOWN:
            if button_rect2.collidepoint(event.pos):
                run=False
            if button_rect3.collidepoint(event.pos):
                pygame.display.iconify()
            if button_rect4.collidepoint(event.pos) and option_state==0:
                  _text2_colour=(150,150,150)
                  option_state=1
            elif button_rect4.collidepoint(event.pos) and option_state==1:
                _text2_colour=(255,255,255)
                option_state=0
            '''if text_rect.collidepoint(event.pos):
                  add_text_op=True
            if text_rect1.collidepoint(event.pos):
                  add_text_op=False
                  homework_data["homeworks"].append(add_text_1)
                  save_homework_data()'''
            if event.button == 5 and h==1:  # Scroll up
                  rect_y -= rect_speed
            elif event.button == 4 and h==1:  # Scroll down
                  rect_y += rect_speed

            if event.button == 5 and s==1:  # Scroll up
                  rect_y1 -= rect_speed
            elif event.button == 4 and s==1:  # Scroll down
                  rect_y1 += rect_speed

            if event.button == 5 and text=="News":  # Scroll up
                  rect_y2 -= rect_speed
            elif event.button == 4 and text=="News":  # Scroll down
                  rect_y2 += rect_speed
            
        if event.type==pygame.MOUSEBUTTONDOWN:
            if button_recta.collidepoint(event.pos):
                  ss=1
                  sss=1
                  aiss=pss=gss=nss=0
            if button_rectb.collidepoint(event.pos):
                  aiss=1
                  sss=pss=gss=nss=0
                  ais=1
            if button_rectc.collidepoint(event.pos):
                  pss=1
                  sss=aiss=gss=nss=0
                  ps=1
            if button_rectd.collidepoint(event.pos):
                  gss=1
                  sss=aiss=pss=nss=0
                  gs=1
            if button_recte.collidepoint(event.pos):
                  nss=1
                  sss=aiss=gss=pss=0
                  ns=1

        if event.type==pygame.MOUSEMOTION:
              if button_rect1.collidepoint(event.pos):
                  search_bar_colour=(100,100,100)
                  search_bar_border_colour=(255,255,255)
                  search_bar_text_colour=(255,255,255)
                  search_icon_state=1
              else:
                  search_bar_colour=(90,90,90)
                  search_bar_border_colour=(150,150,150)
                  search_bar_text_colour=(180,180,180)
                  search_icon_state=0
              if button_rect2.collidepoint(event.pos):
                close_text_colour=(255,255,255)
              else:
                  close_text_colour=(150,150,150)
              if button_rect3.collidepoint(event.pos):
                  _text_colour=(255,255,255)
              else:
                 _text_colour=(150,150,150)
              if button_rect4.collidepoint(event.pos):
                  _text2_colour=(255,255,255)
              elif option_state==1:
                  _text2_colour=(150,150,150)
              if button_recta.collidepoint(event.pos):
                  school_state=1
              else: 
                  school_state=0
              if button_rectb.collidepoint(event.pos):
                  ai_state=1
              else:
                  ai_state=0
              if button_rectc.collidepoint(event.pos):
                  pen_state=1
              else:
                  pen_state=0
              if button_rectd.collidepoint(event.pos):
                  game_state=1
              else:
                  game_state=0
              if button_recte.collidepoint(event.pos):
                  news_state=1
              else:
                  news_state=0
              if text_rect.collidepoint(event.pos):
                  add_colour=(255,255,255)
                  add_text_colour=(255,255,255)
              else:
                  add_colour=(200,200,200)
                  add_text_colour=(140,140,140)
              if text_rect1.collidepoint(event.pos):
                  add_colour1=(255,255,255)
                  add_text_colour1=(255,255,255)
              else:
                  add_colour1=(200,200,200)
                  add_text_colour1=(140,140,140)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                add_text_1 += '\n'
            elif event.key == pygame.K_BACKSPACE:
                add_text_1 = add_text_1[:-1]
            else:
                add_text_1 += event.unicode
      
      
        if event.type == pygame.KEYDOWN:
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
            if event.button == 5:  # Scroll up
                scroll_offset = max(scroll_offset - 20, 0)
            elif event.button == 4:  # Scroll down
                scroll_offset = min(scroll_offset + 20, len(chat_lines) * (font.get_height() + SPACING) - scrollable_area.height)
      
      #Animation
      if option_state==0 and left_rect_state<=100:
        option_state_animation_push()
      elif option_state==1 and left_rect_state>=55:
        option_state_animation_pull()

    #Background
      #top_rect=pygame.draw.rect(screen,(70,70,70),[0,0,winsize[0],30])#Top bar/menu bar
      left2_rect=pygame.draw.rect(screen,(45,45,45),[left_rect_state,32,left2_rect_state,winsize[1]])#option bar pair
      left_rect=pygame.draw.rect(screen,(70,70,70),[0,32,left_rect_state,winsize[1]])#left bar/menu bar
      square=pygame.draw.rect(screen,(45,45,45),[50,squarey,left_rect_state,50])

      #Option in options
      if text=="School":
        school_y=252
        recover=1

        cover_rect=pygame.draw.rect(screen,(30,30,30),[left_rect_state+left2_rect_state,30,winsize[0],winsize[1]])

        s1=pygame.draw.rect(screen,(45,45,45),[left_rect_state,school_y+60*0-2.5,left2_rect_state,30],0,7)
        images[0].draw(screen,left_rect_state+7,school_y+60*0,state1)
        #s2=pygame.draw.rect(screen,(45,45,45),[left_rect_state,school_y+60*1-2.5,left2_rect_state,30],0,7)
        #images[1].draw(screen,left_rect_state+7,school_y+60*1,state2)
        s3=pygame.draw.rect(screen,(45,45,45),[left_rect_state,school_y+60*1-2.5,left2_rect_state,30],0,7)
        images[1].draw(screen,left_rect_state+7,school_y+60*1,state3)
        s4=pygame.draw.rect(screen,(45,45,45),[left_rect_state,school_y+60*2-2.5,left2_rect_state,30],0,7)
        images[2].draw(screen,left_rect_state+7,school_y+60*2,state4)
        s5=pygame.draw.rect(screen,(45,45,45),[left_rect_state,school_y+60*3-2.5,left2_rect_state,30],0,7)
        images[3].draw(screen,left_rect_state+7,school_y+60*3,state5)
        s6=pygame.draw.rect(screen,(45,45,45),[left_rect_state,school_y+60*4-2.5,left2_rect_state,30],0,7)
        images[4].draw(screen,left_rect_state+7,school_y+60*4,state6)

        school_store_text1=font2.render("Home Work",True,colour1)
        school_store_xy1=school_store_text1.get_rect(center=left2_rect.center)
        screen.blit(school_store_text1,(left_rect_state+15+19,school_y+60*0))
        #school_store_text2=font2.render("Circular",True,colour2)
        #school_store_xy2=school_store_text2.get_rect(center=left2_rect.center)
        #screen.blit(school_store_text2,(left_rect_state+15+19,school_y+60*1))
        school_store_text3=font2.render("Attendance",True,colour3)
        school_store_xy3=school_store_text3.get_rect(center=left2_rect.center)
        screen.blit(school_store_text3,(left_rect_state+15+19,school_y+60*1))
        school_store_text4=font2.render("Progress Card",True,colour4)
        school_store_xy4=school_store_text4.get_rect(center=left2_rect.center)
        screen.blit(school_store_text4,(left_rect_state+15+19,school_y+60*2))
        school_store_text5=font2.render("Exam Planner",True,colour5)
        school_store_xy5=school_store_text5.get_rect(center=left2_rect.center)
        screen.blit(school_store_text5,(left_rect_state+15+19,school_y+60*3))
        school_store_text6=font2.render("Special Class",True,colour6)
        school_store_xy6=school_store_text6.get_rect(center=left2_rect.center)
        screen.blit(school_store_text6,(left_rect_state+15+19,school_y+60*4))

        bar=pygame.draw.rect(screen,(30,30,30),[left2_rect_state+left_rect_state-7,school_y+60*tem_x-7.5,7,30+7.5],0,-1,3,-1,3,-1)
        screen.blit(profile_main,(left_rect_state+10,32+30))

        if event.type==pygame.MOUSEBUTTONDOWN:
            if s1.collidepoint(event.pos):
                  h=1
                  c=a=p=e=s=0
                  tem_x=0
            #if s2.collidepoint(event.pos):
             #     c=1
              #    h=a=p=e=s=0
               #   tem_x=1
            if s3.collidepoint(event.pos):
                  a=1
                  h=c=p=e=s=0
                  tem_x=1
            if s4.collidepoint(event.pos):
                  p=1
                  h=a=c=e=s=0
                  tem_x=2
            if s5.collidepoint(event.pos):
                  e=1
                  h=a=p=c=s=0
                  tem_x=3
            if s6.collidepoint(event.pos):
                  s=1
                  h=a=p=e=c=0
                  tem_x=4

        if h==1:
            state1='on'
            colour1=(255,255,255)
        else:
            state1='off'
            colour1=(140,140,140)
        if c==1:
            state2='on'
            colour2=(255,255,255)
        else:
            state2='off'
            colour2=(140,140,140)
        if a==1:
            state3='on'
            colour3=(255,255,255)
        else:
            state3='off'
            colour3=(140,140,140)
        if p==1:
            state4='on'
            colour4=(255,255,255)
        else:
            state4='off'
            colour4=(140,140,140)
        if e==1:
            state5='on'
            colour5=(255,255,255)
        else:
            state5='off'
            colour5=(140,140,140)
        if s==1:
            state6='on'
            colour6=(255,255,255)
        else:
            state6='off'
            colour6=(140,140,140)

        if event.type==pygame.MOUSEMOTION:
            if s1.collidepoint(event.pos):
                 state1='on'
                 colour1=(255,255,255)
            elif h==0:
                state1='off'
                colour1=(140,140,140)
            #if s2.collidepoint(event.pos):
             #    state2='on'
              #   colour2=(255,255,255)
            elif c==0:
                state2='off'
                colour2=(140,140,140)
            if s3.collidepoint(event.pos):
                 state3='on'
                 colour3=(255,255,255)
            elif a==0:
                state3='off'
                colour3=(140,140,140)
            if s4.collidepoint(event.pos):
                 state4='on'
                 colour4=(255,255,255)
            elif p==0:
                state4='off'
                colour4=(140,140,140)
            if s5.collidepoint(event.pos):
                 state5='on'
                 colour5=(255,255,255)
            elif e==0:
                state5='off'
                colour5=(140,140,140)
            if s6.collidepoint(event.pos):
                 state6='on'
                 colour6=(255,255,255)
            elif s==0:
                state6='off'
                colour6=(140,140,140)

        if h==1:
          y_offset = 20
          y_offset += FONT_SIZE + 20

          for hw in homework_data["homeworks"]:
            rect_height = draw_multiline_text_with_rect(screen, hw, (200+left_rect_state, y_offset+rect_y),FONT_SIZE + 5)
            y_offset += rect_height + 10
            
        if a==1:
            get_present_by_name(username)

            mouse_pos = pygame.mouse.get_pos()
            hovered_segment = check_hover(mouse_pos)

            draw_pie_chart(hovered_segment)
            draw_labels()
            draw_legend()

            if hovered_segment == "absent":
              draw_tooltip(mouse_pos, f"Absent: {absent_days} days ({(absent_days / total_days) * 100:.1f}%)")
            elif hovered_segment == "present":
              draw_tooltip(mouse_pos, f"Present: {present_days} days ({(present_days / total_days) * 100:.1f}%)")
                
        if p==1:
            get_marks(username)
            if two==True:
               current_bar_lengths = [0] * len(marks)
               two=False

            title= font3.render("Subject-Wise Marks Distribution", True, WHITE)
            screen.blit(title, (winsize[0] // 2 - title.get_width() // 2+200, 150))

            pygame.draw.line(screen, WHITE, (left_margin-2, top_margin-30), (left_margin-2, top_margin + graph_height+15), 2)  # Y-axis
            pygame.draw.line(screen, WHITE, (left_margin, top_margin + graph_height+15), (left_margin + graph_width, top_margin + graph_height+15), 2)  # X-axis

            for i in range(0, 101, 10): 
               x = left_margin + int((i / 100) * graph_width)
               pygame.draw.line(screen, GRID_COLOR, (x, top_margin), (x, top_margin + graph_height), 1)
               label = font.render(str(i), True, WHITE)
               screen.blit(label, (x - label.get_width() // 2, top_margin + graph_height + 15))

            for i, (subject, mark) in enumerate(zip(subjects, marks)):
               target_length = int((mark / max_mark) * graph_width)
               if current_bar_lengths[i] < target_length:
                 current_bar_lengths[i] += animation_speed
               current_bar_lengths[i] = min(current_bar_lengths[i], target_length)
  
               bar_length = current_bar_lengths[i]
               bar_x = left_margin
               bar_y = top_margin + i * (bar_width + gap)

               pygame.draw.rect(screen, SHADOW, (bar_x + 5, bar_y + 5, bar_length, bar_width))

               for j in range(bar_length):
                  gradient_color = (
                    NEON_BLUE[0] + (NEON_GREEN[0] - NEON_BLUE[0]) * j // bar_length,
                    NEON_BLUE[1] + (NEON_GREEN[1] - NEON_BLUE[1]) * j // bar_length,
                    NEON_BLUE[2] + (NEON_GREEN[2] - NEON_BLUE[2]) * j // bar_length,
                  )
                  pygame.draw.line(screen, gradient_color, (bar_x + j, bar_y), (bar_x + j, bar_y + bar_width))

               subject_text = font6.render(subject, True, WHITE)
               screen.blit(subject_text, (bar_x - 140, bar_y + bar_width // 4))

               if bar_x < mouse_pos[0] < bar_x + bar_length and bar_y < mouse_pos[1] < bar_y + bar_width:
                   tooltip =font.render(f"{subject}: {mark} marks", True, WHITE)
                   pygame.draw.rect(screen, SHADOW, (mouse_pos[0] + 10, mouse_pos[1] - 25, tooltip.get_width() + 10, tooltip.get_height() + 5))
                   pygame.draw.rect(screen, NEON_GREEN, (mouse_pos[0] + 10, mouse_pos[1] - 25, tooltip.get_width() + 10, tooltip.get_height() + 5), 2)
                   screen.blit(tooltip, (mouse_pos[0] + 15, mouse_pos[1] - 23))

               mark_text = font.render(str(mark), True, RED)
               screen.blit(mark_text, (bar_x + bar_length + 10, bar_y + bar_width // 4))

        if e==1:
            screen.blit(test_main,(400,150))

        if s==1:
          y_offset1 = 20
          y_offset1 += FONT_SIZE + 20

          for hw in class_data["class"]:
            rect_height = draw_multiline_text_with_rect(screen, hw, (200+left_rect_state, y_offset1+rect_y1),FONT_SIZE + 5)
            y_offset1 += rect_height + 10

      if text=="ScribeX":
        if recover==1:
           pygame.draw.rect(screen,(30,30,30),[left_rect_state+left2_rect_state,30,winsize[0],winsize[1]])
           recover=0

        box=pygame.Rect(300,32+10,winsize[0]-200-105,winsize[1]-52)
        box_outter=pygame.draw.rect(screen,box_outter_colour,box,2,10)

        subsurface = screen.subsurface(box)

        solve=pygame.draw.rect(screen,solve_colour,[left_rect_state+10,32+10,left2_rect_state-20,left2_rect_state-42],0,10)
        solve_border=pygame.draw.rect(screen,solve_border_colour,[left_rect_state+10,32+10,left2_rect_state-20,left2_rect_state-42],1,10)
        solve_text=font3.render("Solve",True,solve_text_colour)
        solve_text_xy=solve_text.get_rect(center=solve.center)
        screen.blit(solve_text,(solve_text_xy[0],solve_text_xy[1]-30))

        if solve_on:
           screen.blit(main_solve1,(solve_text_xy[0]+18,solve_text_xy[1]+15))
           save_image()
        else:
           screen.blit(main_solve,(solve_text_xy[0]+18,solve_text_xy[1]+15))

        if event.type==pygame.MOUSEBUTTONDOWN:
                if box.collidepoint(event.pos):
                    drawing=True
                    last_pos=event.pos 
        elif event.type==pygame.MOUSEBUTTONUP:
                    drawing=False
        elif event.type==pygame.MOUSEMOTION and drawing:
            # Draw a "brush" at every point the mouse moves
            current_pos = pygame.mouse.get_pos()

            # Draw a circle to simulate the brush effect
            pygame.draw.circle(screen,(255,255,255), current_pos, radius)

            # Optionally, you can draw lines for smoother transitions between circles:
            if last_pos:
                pygame.draw.aaline(screen, (255,255,255), last_pos, current_pos)

            last_pos = current_pos


        if event.type==pygame.MOUSEMOTION:
            if solve.collidepoint(event.pos):
                solve_text_colour=(255,255,255)
                solve_border_colour=(255,255,255)
                solve_on=True
            else:
                solve_text_colour=(140,140,140)
                solve_border_colour=(140,140,140)
                solve_on=False

        if event.type==pygame.MOUSEBUTTONUP:
            if solve.collidepoint(event.pos):
                #solve 
                None

      if text=="News":
          recover=1
          cover_rect=pygame.draw.rect(screen,(30,30,30),[left_rect_state+left2_rect_state,30,winsize[0],winsize[1]])

          y_offset2 = 20
          y_offset2 += FONT_SIZE + 20

          for hw in news_data["news"]:
            rect_height = draw_multiline_text_with_rect(screen, hw, (200+left_rect_state, y_offset2+rect_y2),FONT_SIZE + 5)
            y_offset2 += rect_height + 10

      if text=="VSAI":
          recover=1
          pygame.draw.rect(screen,(30,30,30),[left_rect_state+left2_rect_state,30,winsize[0],winsize[1]])
          
          pygame.draw.rect(screen,(50,50,50),scrollable_area,0,15)
          pygame.draw.rect(screen,(250,250,250),scrollable_area,2,15)

          render_chat(screen, chat_lines, scroll_offset)

          pygame.draw.rect(screen, (70,70,70), input_box, border_radius=15)
          pygame.draw.rect(screen, (250,250,250), input_box,2,15)
          text_surface = font.render(user_input, True, (255,255,255))
          screen.blit(text_surface, (input_box.x + 10, input_box.y + 8))
          
          text_surface1 = font7.render("V", True, (150,150,150))
          screen.blit(text_surface1, (left_rect_state + 50,200))
          text_surface2 = font7.render("S", True, (150,150,150))
          screen.blit(text_surface2, (left_rect_state + 50,300))
          text_surface3 = font7.render("A", True, (150,150,150))
          screen.blit(text_surface3, (left_rect_state + 50,400))
          text_surface4 = font7.render("I", True, (150,150,150))
          screen.blit(text_surface4, (left_rect_state + 50+20, 500))
          
      top_rect=pygame.draw.rect(screen,(70,70,70),[0,0,winsize[0],30])
          
    #Change button colour
      if sss==1:
        coloura=(45,45,45)
        ss=1
        squarey=32
        text="School"
      elif sss==0:
        coloura=(70,70,70)
        ss=0
      if aiss==1:
        colourb=(45,45,45)
        ais=1
        squarey=82
        text="VSAI"
      elif aiss==0:
        colourb=(70,70,70)
        ais=0
      if pss==1:
        ps=1
        colourc=(45,45,45)
        squarey=132
        text="ScribeX"
      elif pss==0:
        ps=0
        colourc=(70,70,70)
      if gss==1:
        gs=1
        colourd=(45,45,45)
        squarey=182
        text="News"
      elif gss==0:
        gs=0
        colourd=(70,70,70)
      if nss==1:
        ns=1
        coloure=(45,45,45)
        squarey=237
        text="N"
      elif nss==0:
        ns=0
        coloure=(70,70,70)
      #Buttons for options
      pygame.draw.rect(screen,coloura,button_recta,0,-1,10,-1,10,-1)
      pygame.draw.rect(screen,colourb,button_rectb,0,-1,10,-1,10,-1)
      pygame.draw.rect(screen,colourc,button_rectc,0,-1,10,-1,10,-1)
      pygame.draw.rect(screen,colourd,button_rectd,0,-1,10,-1,10,-1)
      pygame.draw.rect(screen,coloure,button_recte,0,-1,10,-1,10,-1)

      #Text for options
      option_text=font.render(text,True,(255,255,255))
      if left_rect_state>=100:
       screen.blit(option_text,(50,squarey+15))

      #Search icon/search bar
      search_bar=pygame.draw.rect(screen,search_bar_colour,[winsize[0]-370,4,300,22],0,7)
      search_bar_border=pygame.draw.rect(screen,search_bar_border_colour,[winsize[0]-370,4,300,22],1,7)
      search_bar_text=font.render("Search",True,search_bar_text_colour)
      search_bar_text_xy=search_bar_text.get_rect(center=button_rect1.center)
      screen.blit(search_bar_text,(search_bar_text_xy[0]+15,search_bar_text_xy[1]))
      if search_icon_state==1:
        screen.blit(search_icon_main1,(search_bar_text_xy[0]-5,search_bar_text_xy[1]+2))
      else:
        screen.blit(search_icon_main,(search_bar_text_xy[0]-5,search_bar_text_xy[1]+2))

      #Close and - button
      close_text=font.render("X",True,close_text_colour)
      close_text_xy=close_text.get_rect(center=button_rect2.center)
      screen.blit(close_text,close_text_xy)
      _text=font1.render("-",True,_text_colour)
      _text_xy=_text.get_rect(center=button_rect3.center)
      screen.blit(_text,(_text_xy[0],_text_xy[1]-1))

      #Option menu button
      _text2=font1.render("_",True,_text2_colour)
      _text2_xy=_text2.get_rect(center=button_rect4.center)
      screen.blit(_text2,(_text2_xy[0],_text2_xy[1]-10))
      screen.blit(_text2,(_text2_xy[0],_text2_xy[1]-15))
      screen.blit(_text2,(_text2_xy[0],_text2_xy[1]-20))
      screen.blit(_text2,(_text2_xy[0],_text2_xy[1]-25))
    
      #=========================================[For options]
      #School
      if school_state==0 and ss==0:
       screen.blit(school_main,(school_xy[0],school_xy[1]+5))
      elif school_state==1 or ss==1:
       screen.blit(school_main1,school_xy)
      #AI
      if ai_state==0 and ais==0:
        screen.blit(ai_main,(ai_xy[0],ai_xy[1]+5))
      elif ai_state==1 or ais==1:
        screen.blit(ai_main1,ai_xy)
      #Pen AI
      if pen_state==0 and ps==0:
        screen.blit(pen_main,(pen_xy[0],pen_xy[1]+5))
      elif pen_state==1 or ps==1:
        screen.blit(pen_main1,pen_xy)
      #Games
      if game_state==0 and gs==0:
        screen.blit(news_main,(game_xy[0],game_xy[1]+5+5))
      elif game_state==1 or gs==1:
        screen.blit(news_main1,(game_xy[0],game_xy[1]+5))
      """#news
      if news_state==0 and ns==0:
        screen.blit(news_main,(news_xy[0],news_xy[1]+5))
      elif news_state==1 or ns==1:
        screen.blit(news_main1,(news_xy[0],news_xy[1]))"""
    
      pygame.display.update()
pygame.quit()