import game_framework
from pico2d import *
import main_game
import math
import playboss
name = "StartState"
image = None
logo_time = 0.0
nom=None
talk=None
i=0
be=None
def enter():
    import os
    os.chdir('D:/2016/2d gp/project/image')
    global image,nom,talk,be
    game_framework.reset_time()

    nom=load_image('NOM.png')
    image=load_image('boss.png')
    talk=load_image("talking.png")
    be=load_image("bossba.png")
    pass


def exit():
    global image,nom,talk,be
    del(image)
    del (nom)
    del (talk)
    del(be)

    pass


def update(frame_time):
    global i,z
    i+=1
    if i==5:
        game_framework.change_state(playboss)
    delay(2.5)
    pass


def draw(frame_time):
    clear_canvas()
    be.draw(400,300)
    image.clip_draw(0, 0, 200, 160, 500, 350)
    nom.draw(70,70)
    talk.clip_draw(0,i*100,100,100,650,450)
    talk.clip_draw(100,i*100,100,100,150,180)
    update_canvas()

    pass





def handle_events(frame_time):
    pass


def pause(): pass


def resume(): pass



