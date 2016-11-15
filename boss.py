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
    def __init__(self):
        import os
        os.chdir('D:/2016/2d gp/project/image')
        self.image = load_image('boss.png')
        self.life = 15
        self.attakimage=load_image("bossattack.png")
        self.i=0
        self.x=[500,500,500,500,500,500,500,500,500,500,500,500]
        self.y=[350,350,350,350,350,350,350,350,350,350,350,350]
    def draw(self):
        self.image.clip_draw(0, self.i*160, 200, 160, 400+5*math.cos(Boss.z*Boss.pi), 300+5*math.sin(Boss.z*Boss.pi))
        for i in range(0,12):
            self.attakimage.draw(400+Boss.at*math.cos(i*30*Boss.pi),300+Boss.at*math.sin(i*30*Boss.pi))
            self.x[i]=400+Boss.at*math.cos(i*30*Boss.pi)
            self.y[i]=300+Boss.at*math.sin(i*30*Boss.pi)
        pass
    def update(self,frame_time):

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

    def get_bb(self,i):
        return self.x[i] - 10, self.y[i] - 10, self.x[i] + 10, self.y[i] + 10
