import random
import json
import os
os.chdir('D:/2016/2d gp/project/image')
from pico2d import *
import game_framework
class Boss:
    pi=3.14/180
    z=0
    at=50
    atpoint =200
    ck=0
    def __init__(self):
        import os
        os.chdir('D:/2016/2d gp/project/image')
        self.image = load_image('boss.png')
        self.life = 15
        self.ck=0
        self.i=0

    def draw(self):
        self.image.clip_draw(0, self.i*160, 200, 160, 400+5*math.cos(Boss.z*Boss.pi), 300+5*math.sin(Boss.z*Boss.pi))
        pass
    def update(self,frame_time):
        Boss.ck = self.ck
        if self.life<=10 and self.life>5:
            self.i=1
            Boss.atpoint=300
        if self.life<=5:
            self.i=2
            Boss.atpoint = 400
        Boss.z+=500*frame_time
        Boss.at+=Boss.atpoint*frame_time
        if(Boss.at>=450):
            Boss.at=50
            self.ck=0
            Boss.ck=self.ck
class BossAttack:
    def __init__(self):
        self.attakimage = load_image("bossattack.png")
        self.x = 500
        self.y = 350
        self.i=random.randint(0, 12)
    def draw(self):
        if(Boss.ck==0):
            self.attakimage.draw(400+Boss.at*math.cos(self.i*30*Boss.pi),300+Boss.at*math.sin(self.i*30*Boss.pi))
            self.x=400+Boss.at*math.cos(self.i*30*Boss.pi)
            self.y=300+Boss.at*math.sin(self.i*30*Boss.pi)
        pass

    def update(self, frame_time):
        if(Boss.at==50):
            self.i = random.randint(0, 12)
        pass
    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10