import random
import json
import os
import math
os.chdir('D:/2016/2d gp/project/image')

from pico2d import *
import game_framework
import title
import bossready
class boss:
    pi=3.14/180
    def __init__(self):
        import os
        os.chdir('D:/2016/2d gp/project/image')
        self.image = load_image('boss.png')
        self.life = 15
        self.attakimage=load_image("bossattack.png")
        self.i=0
    def draw(self):
        self.image.clip_draw(0, self.i*100, 100, 100, 500, 350)
        pass
    def update(self):
        if self.life==10:
            self.i=1
        if self.life==5:
            self.i=2