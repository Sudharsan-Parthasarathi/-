import pygame
from pygame.locals import *
import time
import json
import os

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
radius=3
username = ""
password = ""
username_active = False
password_active = False
dis_name=False
dis_pass=False
i_pass=False
FONT_SIZE=20
add_text_op=False
rect_y=0
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
            if text_rect.collidepoint(event.pos):
                  add_text_op=True
            if text_rect1.collidepoint(event.pos):
                  add_text_op=False
                  homework_data["homeworks"].append(add_text_1)
                  save_homework_data()
            if event.button == 5:  # Scroll up
                  rect_y -= rect_speed
            elif event.button == 4:  # Scroll down
                  rect_y += rect_speed
            
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

        cover_rect=pygame.draw.rect(screen,(30,30,30),[left_rect_state+left2_rect_state,32,winsize[0],winsize[1]])

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

        #homework======================================================================================================================
        if h==1:
          y_offset = 20
          y_offset += FONT_SIZE + 20

          for hw in homework_data["homeworks"]:
            rect_height = draw_multiline_text_with_rect(screen, hw, (200+left_rect_state, y_offset+rect_y),FONT_SIZE + 5)
            y_offset += rect_height + 10
            
          rect_xy=pygame.draw.rect(screen,(50,50,50),text_add_rect,0,10)
          pygame.draw.rect(screen,add_colour,text_add_rect,2,10)
          add_text=font6.render("Add Work",True,add_text_colour)
          add_text_xy=add_text.get_rect(center=rect_xy.center)
          screen.blit(add_text,add_text_xy)

          if add_text_op==True:
              input_box=pygame.draw.rect(screen,(50,50,50),[winsize[0]//2-400,winsize[1]//2-300,800,600],0,15)
              pygame.draw.rect(screen,(255,255,255),[winsize[0]//2-400,winsize[1]//2-300,800,600],3,15)
              rect_xy1=pygame.draw.rect(screen,(50,50,50),text_add_rect1,0,10)
              pygame.draw.rect(screen,add_colour1,text_add_rect1,2,10)
              add_text1=font6.render("Done",True,add_text_colour1)
              add_text_xy1=add_text1.get_rect(center=rect_xy1.center)
              screen.blit(add_text1,add_text_xy1)
              lines1 = render_text()
              for i, line1 in enumerate(lines1):
                screen.blit(line1, (input_box.x+10,input_box.y+10+ i * line_height1))
                
      if text=="Bot2":
        cover_rect=pygame.draw.rect(screen,(30,30,30),[left_rect_state+left2_rect_state,32,10,winsize[1]])

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
                    current_pos=pygame.mouse.get_pos()
                    if box.collidepoint(current_pos):
                      if last_pos and box.collidepoint(last_pos):
                       pygame.draw.line(screen,cv_colour,last_pos,current_pos,radius)
                      last_pos=current_pos

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
        text="Bot1"
      elif aiss==0:
        colourb=(70,70,70)
        ais=0
      if pss==1:
        ps=1
        colourc=(45,45,45)
        squarey=132
        text="Bot2"
      elif pss==0:
        ps=0
        colourc=(70,70,70)
      if gss==1:
        gs=1
        colourd=(45,45,45)
        squarey=182
        text="Games"
      elif gss==0:
        gs=0
        colourd=(70,70,70)
      if nss==1:
        ns=1
        coloure=(45,45,45)
        squarey=237
        text="News"
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
        screen.blit(game_main,(game_xy[0],game_xy[1]+5))
      elif game_state==1 or gs==1:
        screen.blit(game_main1,game_xy)
      #news
      if news_state==0 and ns==0:
        screen.blit(news_main,(news_xy[0],news_xy[1]+5))
      elif news_state==1 or ns==1:
        screen.blit(news_main1,(news_xy[0],news_xy[1]))
    
      pygame.display.update()
pygame.quit()