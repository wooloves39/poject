import random
import json
import os
os.chdir('D:/2016/2d gp/project/image')
import title
from pico2d import *
import game_framework
class Nom:
    stage=0
    speed=20
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
        self.powerup=0
    def update(self,frame_time):
        global stage
        if self.state==4:
            self.jumping=0
        self.timer+=1
        self.frame=(self.frame+1)%self.framestate
        self.jump()
        self.jump2()
        self.damage()
        if self.timer<=10:
            self.powerup=1
        else:
            self.powerup=0
        if self.timer>=100:
            self.powerup=1
            if Nom.stage==0:
                self.x+=Nom.speed
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
                        Nom.stage=1
                        self.powerup = 0
            elif Nom.stage==1:
                self.y+=Nom.speed
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
                        Nom.stage=2
                        self.powerup = 0
                pass
            elif Nom.stage==2:
                self.x-=Nom.speed
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
                        Nom.stage=3
                        self.powerup = 0
                pass
            elif Nom.stage==3:
                self.y-=Nom.speed
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
                        Nom.stage=0
                        self.powerup = 0
                pass
            pass
    def damage(self):
        if (self.life <= 0):
            game_framework.change_state(title)
        if(self.powerup==1):
            self.state = Nom.stage
            self.attaktime = 0
        if((self.state==5 or self.state==6 or self.state==7 or self.state==8)and self.frame==5):
            self.life-=1
            self.state=Nom.stage
            self.attaktime=0

    def jump2(self):
        if self.jumping == 2:
            if Nom.stage == 0:
                delay(0.01 - 0.05 * (Nom.speed / 400))
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
            elif Nom.stage == 1:

                delay(0.01 - 0.05 * (Nom.speed / 400))
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
            elif Nom.stage == 2:

                delay(0.01 - 0.05 * (Nom.speed / 400))
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
            elif Nom.stage == 3:

                delay(0.01 - 0.05 * (Nom.speed / 400))
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
                delay(0.01 - 0.05*(Nom.speed / 400))
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
                delay(0.01 - 0.05 * (Nom.speed / 400))
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
                delay(0.01 - 0.05 * (Nom.speed / 400))
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
                delay(0.01 - 0.05 * (Nom.speed / 400))
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
            Nom.speed = min(Nom.speed + 5, 40)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            Nom.speed = min(Nom.speed - 5, 40)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.jumping == 1:
                self.jumping = 2
            elif self.jumping == 0:
                self.jumping = 1
            pass
    def draw(self):
        self.image.clip_draw(self.frame*100,self.state*100,100,100,self.x,self.y)
        delay(0.1 - self.speed / 400)

    def get_bb(self):
        return self.x - 25, self.y - 50, self.x + 25, self.y + 50
class Life:
    def __init__(self):
        import os
        os.chdir('D:/2016/2d gp/project/image')
        self.image = load_image('nomlife.png')
        self.switch=3
    def draw(self):
        if(Nom.stage==0):
            for i in range(self.switch):
                self.image.clip_draw(0, Nom.stage*50, 50, 50, 350+i*50, 520)

        elif(Nom.stage==1):
            for i in range(self.switch):
                self.image.clip_draw(0, Nom.stage*50, 50, 50, 80, 250+i*50)
        elif (Nom.stage == 2):
            for i in range(self.switch):
                self.image.clip_draw(0, Nom.stage * 50, 50, 50, 450 - i * 50, 800)
        elif (Nom.stage == 3):
            for i in range(self.switch):
                self.image.clip_draw(0, Nom.stage * 50, 50, 50, 720, 350-i*50)
        pass
    pass