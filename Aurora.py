import pygame
import time
import pygame.gfxdraw
import random

background1 = pygame.image.load('img/background.png')
background2 = pygame.image.load('img/background.png')
pygame.init()
my_font = pygame.font.Font("fonts/Pixel.ttf",24)
for_name_font = pygame.font.Font("fonts/Pixel.ttf",70)
car_player_image = pygame.image.load('img/space.png')
rocket = pygame.image.load('img/rocket.png')
car_enemy_down = pygame.image.load('img/bad_car.png')
free_game_btn = pygame.image.load('img/free.png')
mission = pygame.image.load('img/mission.png')
cursor = pygame.image.load('img/cursor.png')
shot_snd = pygame.mixer.music.load('music/shot_msc.mp3')
help_btn = pygame.image.load('img/help_btn.png')
back_btn = pygame.image.load('img/back_btn.png')
explosion1 = pygame.image.load('img/explosion1.png')
explosion2 = pygame.image.load('img/explosion2.png')
explosion3 = pygame.image.load('img/explosion3.png')
explosion4 = pygame.image.load('img/explosion4.png')
explosion5 = pygame.image.load('img/explosion5.png')
explosion6 = pygame.image.load('img/explosion6.png')
rocket_slide = pygame.image.load('img/rocket_slide.png')
pygame.mixer.music.set_volume(0.1)

speed = 3
cur_frame = 0
frames = [explosion1,explosion2,explosion3,explosion4,explosion5,explosion6]
volume = 0
background_y = 0
display_w = 800
display_h = 600
game_exit = False
stop = False
score_shot = 0
score_arr = []
bad_line = 0
white = [255,255,255]
black = [0,0,0]
game_display = pygame.display.set_mode((display_w, display_h))
shot_rocket = False
world_speed = 7
car_line = 0
line_x = 0
shot_y = 400
die = False
restart = False
green = [0,255,0]
rand = 31
click_pos = 0
x=990
y=990
mouse = 0
free_click = False
mis_click = False
help = False

class car:
    image = None
    direction = 0
    speed = 0
    visible = True
    
    def __init__(self,image,direction = 0,speed = 3):
        self.image = image
        self.direction = direction
        self.speed = speed
        

class player_car(car):
    global line_x
    
        
class enemy_car(car):
    car_y = 0 
    car_line = 0
    def __init__(self,direction = 0,car_line = 0,speed = 1):
        self.visible = False
        if (direction == 1):
            self.image = car_enemy_down
            self.car_y = -20
        
        self.direction = direction
        self.speed = speed 
        
    def draw(this):
        global bad_line,die,score_arr,speed
        if (this.visible == True):
            if (this.direction == 1):
                this.car_y += this.speed   
            
                
            game_display.blit(car_enemy_down,(335 + bad_line * 170, this.car_y))
            if(this.car_y >700) or (this.car_y<-200):
                this.visible = False   
            if this.car_y >700:
                die = True
                speed = 3
                if free_click:
                    score_arr.append(score_shot)
 
    def check_collision(this, to_check):
        global rocket_rect,car_y,bad_line,shot_y,die,score_shot,score_arr,speed,mouse,mis_click,free_click,x,y,help,cur_frame
        rocket_rect =rocket.get_rect().move(370 + car_line* 170, shot_y)
        to_check_rect = to_check.image.get_rect().move(370 + bad_line * 170,this.car_y)
        my_rect = car_player_image.get_rect().move(370 + car_line* 170,400)
        btn_free_rect = free_game_btn.get_rect().move(100,450)
        btn_mis_rect = mission.get_rect().move(520,450)
        if help == False:
            help_btn_rect = help_btn.get_rect().move(0,0)
        if help == True:
            back_btn_rect = back_btn.get_rect().move(0,0)
        mouse = pygame.Rect((x,y),(1,1))
        if rocket_rect.colliderect(to_check_rect):
            this.visible = False
            if shot_rocket == True:
                score_shot+=1
            
            return True
        if my_rect.colliderect(to_check_rect):
            die = True
            if free_click:
                score_arr.append(score_shot)
            speed = 3
        if btn_free_rect.colliderect(mouse):
            free_click = True
            mis_click =False
            die = False
            score_shot = 0
            x = 900
            y = 900
            cur_frame = 0
        if btn_mis_rect.colliderect(mouse):
            mis_click = True
            free_click = False
            die = False
            score_shot = 0            
            x = 900
            y = 900
            cur_frame = 0
        if help == False:
            if help_btn_rect.colliderect(mouse):
                help = True
                x = 900
                y = 900
        elif help == True:
            if back_btn_rect.colliderect(mouse):
                help = False
                x = 900
                y = 900        
   
    def reset(this):
        global bad_line,speed
        
        this.visible = True
        this.direction = 1
        bad_line = random.randint(-1,1)
        if (this.direction == 1):
            this.image = car_enemy_down
            this.car_y = -100
        
        this.speed = speed
rck = player_car(rocket)

enemy_cars = [enemy_car(1, 1, 3),enemy_car(1, 0, 1),enemy_car(0, 1, 2),enemy_car(0, 0, 5)]

pygame.display.set_caption('Aurora.exe')
clock = pygame.time.Clock()

def process_keyboard(event):  
    global car_line,world_speed,shot_y,shot_rocket, restart,die,score_shot,speed,x,y,mouse
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            car_line -= 1
            if car_line == -2:
                car_line = -1           
        if event.key == pygame.K_RIGHT:
            car_line += 1
            if car_line == 2:
                car_line =1             
        if die == False and score_shot <rand and mis_click == True:
            if event.key == pygame.K_SPACE:
                
                shot_rocket = True
                pygame.mixer.music.play()
                speed +=0.09
        if die == False and free_click == True:
            
            if event.key == pygame.K_SPACE:
                
                pygame.mixer.music.play()
                shot_rocket = True
                speed +=0.05               
       
    if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1:
            x, y = event.pos
    
    pygame.mouse.set_visible(False)
  
def draw_enemys():
    import random
    for car in enemy_cars:
        if car.visible == False:
            if random.randint(1,1) == 1:
                if die == False and mis_click == True and score_shot <rand:
                    car.reset()
                if free_click == True and die == False:
                    car.reset()
        car.check_collision(rck)
    for i in enemy_cars:
        car.draw()
def draw_UI():
    global car_line, line_x, shot_rocket,bad_line,die,score_shot,mouse,speed,cur_frame
    mshp = my_font.render("MSHP inc", True, (0,255,0))
    name = for_name_font.render("Aurora.exe", True, (0,255,0))
    score = my_font.render(str(score_shot), True, (255,255,255))
    record1 = my_font.render("Ваш рекорд - ", True, (255,255,255))
    record2 = my_font.render(str(max(score_arr, default=99)), True, (255,255,255))
    info1 = my_font.render("Возле планеты 4546B на космический корабль Аврора", True, (255,255,255))
    info11 = my_font.render("напали инопланетные захватчики!", True, (255,255,255))
    info2 = my_font.render("Помоги капитану спасти жизни экипажа", True, (255,255,255))
    info22 = my_font.render("И выбраться из окружения", True, (255,255,255))
    info3 =  my_font.render("Скорость вржеских кораблей увеличивается,аккуратнее!", True, (255,0,0))
    help_txt1 = my_font.render("Чтобы двигаться используйте стрелки на клавиатуре.", True, (0,255,0))
    help_txt2 = my_font.render("Чтобы стрелять нажимайте Пробел", True, (0,255,0))
    die_txt1 = my_font.render(("К сожалению, Ваш космический корабль унижточен"), True, (255,255,255))
    
    win = my_font.render(("Браво! Вы смогли пережить нападение!"), True, (0,255,0)) 
    if mis_click!= True and free_click == False and help == False:
        game_display.blit(name, (240,200))
        game_display.blit(help_btn, (0,0))
        game_display.blit(mshp, (500,280))
    if die == True :
        game_display.blit(die_txt1, (90,300))
        game_display.blit(help_btn, (0,0))

        if mis_click == False and free_click == True:
            game_display.blit(record1, (300,420))
            game_display.blit(record2, (480,420))
                         
    if die == False and score_shot <rand and mis_click:
        game_display.blit(score, (0,0))
        #Пасхалка! :)
        #Тулезх ПЫТ! Шифр Цезаря сдвиг - 3
        pygame.draw.line(game_display, green, [0,0], [25*score_shot,0], 10)
        game_display.blit(rocket_slide,((25*score_shot,-8)))
    if free_click == True and die == False:
        game_display.blit(score, (0,0))
        
    if score_shot >=rand and die == False and mis_click == True and help == False:
        game_display.blit(win, (150,250))
        game_display.blit(free_game_btn, (100,450))
        game_display.blit(mission, (520,450))
        game_display.blit(cursor, (pygame.mouse.get_pos()))
        speed = 3
        
    if free_click == False and mis_click == False and help == False:
        game_display.blit(free_game_btn, (100,450))
        game_display.blit(mission, (520,450))
    if die == True:
        game_display.blit(free_game_btn, (100,450))
        game_display.blit(mission, (520,450))
                
    pygame.draw.rect(game_display, black, mouse, 0)
    if free_click == False and mis_click == False:
        game_display.blit(cursor, (pygame.mouse.get_pos()))
        
    if die == True:
        game_display.blit(cursor, (pygame.mouse.get_pos()))
    
    if help == True:
        game_display.blit(info1, (50,100))
        game_display.blit(info11, (50,140))
        game_display.blit(info2, (50,180))
        game_display.blit(info3, (50,260))
        game_display.blit(info22, (50,220))   
        game_display.blit(help_txt1, (50,340))   
        game_display.blit(help_txt2, (150,380))   
        game_display.blit(back_btn, (2,2))
    
       
    if die == True:
        if cur_frame < len(frames)-1:
                cur_frame +=1  
                game_display.blit(frames[cur_frame],(300+car_line*180,400))
    
def shot():
    global shot_rocket, shot_y
    if shot_rocket:
        shot_y -=50
        if shot_y > 0:
            for i in range(shot_rocket):
                
                game_display.blit(rocket,(370 + car_line * 180,shot_y))  
        else:
            shot_rocket = False
            shot_y = 600
    
def draw_background():
    global background_y, world_speed,car_line
    game_display.blit(background1,(0,background_y))
    game_display.blit(background2,(0,background_y - 600))
    if background_y >= display_h:
        background_y = display_h - 600
    if die == False:
        game_display.blit(car_player_image,(300+car_line*180,400))
    background_y += world_speed 

def game_loop(update_time):
    global game_exit,cur_frame
    while not game_exit:
        for event in pygame.event.get():
            process_keyboard(event)
            if event.type == pygame.QUIT:
                game_exit = True
                pygame.quit()
        draw_background()   
        draw_enemys()
        draw_UI()
        shot()
        pygame.display.update()
        clock.tick(update_time)     

game_loop(30)
pygame.quit()
