import random
import json
import os
os.chdir('D:/2016/2d gp/project/image')
from pico2d import *
import game_framework
class attack_item:
    pi=3.14/180
    z=0
    speed=20
    atpoint =200
    ck=0
    def __init__(self):
        import os
        os.chdir('D:/2016/2d gp/project/image')
        self.image = load_image('nomattack.png')
        self.x=800
        self.y=80
        self.state=0
        self.timer = random.randint(0, 100)*5
        self.ck=0
    def draw(self):
        if(self.timer==0):
            self.image.draw(self.x ,self.y)

        pass
    def update(self,frame_time,stage):
        print(self.timer)
        if self.ck==0:
            if(stage!=self.state):
                self.chstate(stage)
            if self.timer != 0:
                self.timer -= 1
            if self.timer == 0:
                if self.state == 0:
                    self.x -= attack_item.speed
                    if self.x <= 0:
                        self.x = 800
                        self.timer = random.randint(0, 100)*5
                elif self.state == 1:
                    self.y -= attack_item.speed
                    if self.y <= 0:
                        self.y = 600
                        self.timer = random.randint(0, 100)*5
                elif self.state == 2:
                    self.x += attack_item.speed
                    if self.x >= 800:
                        self.x = 0
                        self.timer = random.randint(0, 100)*5
                elif self.state == 3:
                    self.y += attack_item.speed
                    if self.y >= 600:
                        self.y = 0
                        self.timer = random.randint(0, 100)*5
            self.get_bb()
        elif self.ck == 1:
            if self.x<=400:
                self.x+=attack_item.speed
            elif self.x>400:
                self.x -= attack_item.speed
            if self.y<=300:
                self.y += attack_item.speed
            elif self.y>300:
                self.y -= attack_item.speed
            pass

    def chstate(self,stage):
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

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
class bonus_item:
    def __init__(self):
        self.image = load_image("heart.png")
        self.x = 800
        self.y = 80
        self.i=0
        self.state = 0
        self.timer = random.randint(0, 100)*5
        self.sw=0
    def draw(self):
        if(self.sw==0):
            if (self.timer == 0):
                self.image.clip_draw(0, self.state * 50, 50, 50, self.x, self.y)
        pass
    def update(self, frame_time, stage):
        print(self.timer)
        if (stage != self.state):
            self.chstate(stage)
        if self.timer != 0:
            self.timer -= 1
        if self.timer == 0:
            if self.state == 0:
                self.x -= attack_item.speed
                if self.x <= 0:
                    self.x = 800
                    self.timer = random.randint(0, 100)*5
                    self.sw=0
            elif self.state == 1:
                self.y -= attack_item.speed
                if self.y <= 0:
                    self.y = 600
                    self.timer = random.randint(0, 100)*5
                    self.sw = 0
            elif self.state == 2:
                self.x += attack_item.speed
                if self.x >= 800:
                    self.x = 0
                    self.timer = random.randint(0, 100)*5
                    self.sw = 0
            elif self.state == 3:
                self.y += attack_item.speed
                if self.y >= 600:
                    self.y = 0
                    self.timer = random.randint(0, 100)*5
                    self.sw = 0
        self.get_bb()
    def chstate(self, stage):
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

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25