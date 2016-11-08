import random
import json
import os

os.chdir('D:/2016/2d gp/project/image')

from pico2d import *
import game_framework
import title

name='MAIN GAME'
life=None
nom=None
baground=None
font=None
attack=None
attack1=None
speed=20
stage=0
score=0
font=None
backg=None
class Life:
    def __init__(self):
        import os
        os.chdir('D:/2016/2d gp/project/image')
        self.image = load_image('nomlife.png')
        self.switch=3
    def draw(self):
        global stage
        if(stage==0):
            for i in range(self.switch):
                self.image.clip_draw(0, stage*50, 50, 50, 350+i*50, 550)
        elif(stage==1):
            for i in range(self.switch):
                self.image.clip_draw(0, stage*50, 50, 50, 50, 250+i*50)
        elif (stage == 2):
            for i in range(self.switch):
                self.image.clip_draw(0, stage * 50, 50, 50, 450 - i * 50, 50)
        elif (stage == 3):
            for i in range(self.switch):
                self.image.clip_draw(0, stage * 50, 50, 50, 750, 350-i*50)
        pass
    pass
class Background:
    def __init__(self):
        import os
        os.chdir('D:/2016/2d gp/project/image')
        self.image=load_image('background.png')
        self.frame=random.randint(0,4)
        self.changemap=stage
    def update(self):
        if self.changemap!=stage:
            self.frame=random.randint(0,4)
            self.changemap=stage
    def draw(self):
        self.image.clip_draw(self.frame * 800, 0, 800, 600, 400, 300)
class Baground:
    def __init__(self):
        import os
        os.chdir('D:/2016/2d gp/project/image')
        self.image=load_image('back.png')

    def draw(self):
        self.image.draw(400,30)
        self.image.draw(800,30)
class Nom:
    def __init__(self):
        import os
        os.chdir('D:/2016/2d gp/project/image')
        self.x,self.y=70,80
        self.frame=0
        self.life=3
        self.image=load_image('nomrunver2.png')
        self.dir=1
        self.jump_frames1=0
        self.jump_frames2 = 0
        self.jumping=0
        self.timer=0
        self.state=0
        self.framestate=8
        self.attaktime=0
    def update(self):
        global stage
        if self.state==4:
            self.jumping=0
        self.timer+=1
        self.frame=(self.frame+1)%self.framestate
        self.jump()
        self.jump2()
        self.damage()
        if self.timer>=100:
            if stage==0:
                self.x+=speed
                if self.x>=600:
                    self.state=4
                    self.framestate=6
                    self.attaktime=0
                    if self.x>=700 :
                        self.x=720
                        self.y=70
                        self.timer=0
                        self.state=1
                        self.framestate = 8
                        stage=1
            elif stage==1:
                self.y+=speed
                if self.y>=400:
                    self.state=4
                    self.framestate = 6
                    self.attaktime = 0
                    if self.y>=500:
                        self.y=520
                        self.x=730
                        self.timer=0
                        self.state=2
                        self.framestate = 8
                        stage=2
                pass
            elif stage==2:
                self.x-=speed
                if self.x<=170:
                    self.state=4
                    self.framestate = 6
                    self.attaktime = 0
                    if self.x<=70:
                        self.x=80
                        self.y=530
                        self.timer = 0
                        self.state = 3
                        self.framestate = 8
                        stage=3
                pass
            elif stage==3:
                self.y-=speed
                if self.y<=180:
                    self.state=4
                    self.framestate = 6
                    self.attaktime = 0
                    if self.y<=80:
                        self.y=80
                        self.x=70
                        self.timer=0
                        self.state=0
                        self.framestate = 8
                        stage=0
                pass
            pass
    def damage(self):
        global stage
        global life
        if (self.life == 0):
            game_framework.change_state(title)
        if((self.state>=5)and self.frame==5):
            self.life-=1
            self.state=stage
            self.attaktime=0
            life.switch-=1

    def jump2(self):
        if self.jumping == 2:
            if stage == 0:
                delay(0.01 - 0.05 * (speed / 400))
                self.jump_frames2 += 1
                if self.jump_frames2 < 6:
                    self.y += 28
                elif self.jump_frames2 >= 6 and self.jump_frames2 < 11+self.jump_frames1 and self.y>80:
                    self.state=0
                    self.y -= 28

                else:
                    self.jump_frames1 = 0
                    self.jump_frames2 = 0
                    self.jumping = 0
            elif stage == 1:

                delay(0.01 - 0.05 * (speed / 400))
                self.jump_frames2 += 1
                if self.jump_frames2 < 6:
                    self.x -= 28
                elif self.jump_frames2 >= 6 and self.jump_frames2 < 11+self.jump_frames1 and self.x<720:
                    self.state = 1
                    self.x += 28
                else:
                    self.jump_frames1 = 0
                    self.jump_frames2 = 0
                    self.jumping = 0
            elif stage == 2:

                delay(0.01 - 0.05 * (speed / 400))
                self.jump_frames2 += 1
                if self.jump_frames2 < 6:
                    self.y -= 28
                elif self.jump_frames2 >= 6 and self.jump_frames2 < 11+self.jump_frames1 and self.y<520:
                    self.state = 2
                    self.y += 28
                else:
                    self.jump_frames1 = 0
                    self.jump_frames2 = 0
                    self.jumping = 0
            elif stage == 3:

                delay(0.01 - 0.05 * (speed / 400))
                self.jump_frames2 += 1
                if self.jump_frames2 < 6:
                    self.x += 28
                elif self.jump_frames2 >= 6 and self.jump_frames2 < 11+self.jump_frames1 and self.x>80:
                    self.state = 3
                    self.x -= 28
                else:
                    self.jump_frames1 = 0
                    self.jump_frames2 = 0
                    self.jumping = 0
            pass

    pass

    def jump(self):
        if self.jumping==0:
            self.jump_frames1=0
            self.jump_frames2 = 0
            pass
        elif self.jumping == 1:
            if self.state==0:
                delay(0.01 - 0.05*(speed / 400))
                self.jump_frames1 += 1
                if self.jump_frames1 < 6:
                    self.y += 28
                elif self.jump_frames1 >= 6 and self.jump_frames1 < 11:
                    self.y -= 28
                else:
                    self.jump_frames1 = 0
                    self.jump_frames2 = 0
                    self.jumping = 0
            elif self.state==1:
                delay(0.01 - 0.05 * (speed / 400))
                self.jump_frames1 += 1
                if self.jump_frames1 < 6:
                    self.x -= 28
                elif self.jump_frames1 >= 6 and self.jump_frames1 < 11:
                    self.x += 28
                else:
                    self.jump_frames1 = 0
                    self.jump_frames2 = 0
                    self.jumping = 0
            elif self.state == 2:
                delay(0.01 - 0.05 * (speed / 400))
                self.jump_frames1 += 1
                if self.jump_frames1 < 6:
                    self.y -= 28
                elif self.jump_frames1 >= 6 and self.jump_frames1 < 11:
                    self.y += 28
                else:
                    self.jump_frames1 = 0
                    self.jump_frames2 = 0
                    self.jumping = 0
            elif self.state==3:
                delay(0.01 - 0.05 * (speed / 400))
                self.jump_frames1 += 1
                if self.jump_frames1 < 6:
                    self.x += 28
                elif self.jump_frames1 >= 6 and self.jump_frames1 < 11:
                    self.x -= 28
                else:
                    self.jump_frames1 = 0
                    self.jump_frames2 = 0
                    self.jumping = 0
            pass
    pass
    def handle_event(self, event):
        global speed
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_u):
            speed = min(speed + 5, 40)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            speed = min(speed - 5, 40)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.jumping == 1:
                self.jumping = 2
            elif self.jumping == 0:
                self.jumping = 1
            pass
    def draw(self):
        self.image.clip_draw(self.frame*100,self.state*100,100,100,self.x,self.y)

class Attack:
    def __init__(self):
        import os
        os.chdir('D:/2016/2d gp/project/image')
        self.image=load_image('attackver2.png')
        self.x=800
        self.y=80
        self.state=0
        self.drop=random.randint(0,10)%5
        self.timer=random.randint(0,100)*5
    def draw(self):
        if self.timer==0:
            self.image.clip_draw(self.drop*100,self.state*100,100,100,self.x,self.y)
    def update(self):
        global stage
        if stage != self.state:
            self.chstate()
        if self.timer != 0:
            self.timer -= 1
        if self.timer==0:
            if self.state==0:
                self.x -= speed
                if self.x <= 0:
                    self.x = 800
                    self.timer=random.randint(0,100)*5
            elif self.state==1:
                self.y-=speed
                if self.y<=0:
                    self.y=600
                    self.timer = random.randint(0, 100) * 5
            elif self.state == 2:
                self.x += speed
                if self.x >= 800:
                    self.x = 0
                    self.timer = random.randint(0, 100) * 5
            elif self.state == 3:
                self.y += speed
                if self.y >= 600:
                    self.y = 0
                    self.timer = random.randint(0, 100) * 5
    def chstate(self):
        global stage
        if stage == 0:
            self.state = 0
            self.x = 800
            self.y = 80
            pass
        elif stage == 1:
            self.state = 1
            self.x = 720
            self.y = 600
            pass
        elif stage == 2:
            self.state = 2
            self.x, self.y = 0, 520
            pass
        elif stage == 3:
            self.state = 3
            self.x, self.y = 80, 0
            pass
def damagenom():
    global nom
    global attack
    global stage
    global life
    for i in attack:
        if(nom.attaktime==0):
            if(stage==0):
                if (nom.x <= i.x and nom.x+80>=i.x and nom.y <= i.y and nom.y<=i.y+80 ):
                    nom.state=nom.state+5
                    nom.frame=0
                    nom.attaktime=1

            elif(stage==1):
                if (nom.x <= i.x and nom.x+80>=i.x and nom.y+80 >= i.y and nom.y<=i.y ):
                    print(12)
                    nom.state=nom.state+5
                    nom.frame=0
                    nom.attaktime=1

            elif (stage == 2):
                if (nom.x <= i.x+80 and nom.x + 80 >= i.x+80 and nom.y >= i.y and nom.y+80 >= i.y):
                    nom.state = nom.state + 5
                    nom.frame = 0
                    nom.attaktime = 1

            elif (stage == 3):
                if (nom.x <= i.x+80and nom.x + 80 >= i.x+80 and nom.y <= i.y+80 and nom.y+80 >= i.y + 80):
                    nom.state = nom.state + 5
                    nom.frame = 0
                    nom.attaktime = 1
            pass

def enter():
    global nom,baground,attack,back,life,font
    nom=Nom()
    baground=Baground()
    life=Life()
    i=0
    font=load_font('ENCR10B.TTF')
    attack=[Attack() for i in range(10)]
    back=Background()

    pass


def exit():
    global nom, baground, attack, back,font
    del(nom)
    del(baground)
    del(attack)
    del(back)
    del(life)
    del(font)
    pass
def pause():
    pass

def resume():
    pass

def handle_events():
    global speed
    global nom
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type ==SDL_KEYDOWN and event.key== SDLK_ESCAPE:
                game_framework.change_state(title)
        else:
            nom.handle_event(event)



    pass

def update():
    global attack,score
    score+=1
    print(score)
    back.update()
    nom.update()
    for i in attack:
        i.update()
    damagenom()

    pass
def draw():
    global speed,attack,score
    clear_canvas()
    back.draw()
    baground.draw()
    nom.draw()
    life.draw()
    font.draw(40,30,'sdasd')
    for i in attack:
        i.draw()
    update_canvas()
    delay(0.1-speed/400)
    pass