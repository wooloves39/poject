import random
import json
import os
os.chdir('D:/2016/2d gp/project/image')
import title
from pico2d import *
import game_framework

class Attack:
    speed=20
    def __init__(self):
        import os
        os.chdir('D:/2016/2d gp/project/image')
        self.image=load_image('attackver2.png')
        self.x=800
        self.y=65
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
                self.x -= Attack.speed
                if self.x <= 0:
                    self.x = 800
                    self.timer=random.randint(0,100)*5
            elif self.state==1:
                self.y-=Attack.speed
                if self.y<=0:
                    self.y=600
                    self.timer = random.randint(0, 100) * 5
            elif self.state == 2:
                self.x += Attack.speed
                if self.x >= 800:
                    self.x = 0
                    self.timer = random.randint(0, 100) * 5
            elif self.state == 3:
                self.y += Attack.speed
                if self.y >= 600:
                    self.y = 0
                    self.timer = random.randint(0, 100) * 5
    def chstate(self):
        global stage
        if stage == 0:
            self.state = 0
            self.x = 800
            self.y = 65
            pass
        elif stage == 1:
            self.state = 1
            self.x = 735
            self.y = 600
            pass
        elif stage == 2:
            self.state = 2
            self.x, self.y = 0, 535
            pass
        elif stage == 3:
            self.state = 3
            self.x, self.y = 65, 0
            pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25