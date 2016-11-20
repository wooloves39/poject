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
bgm1=None
bgm2=None
z=0
def enter():
    import os
    os.chdir('D:/2016/2d gp/project/image')
    global image,nom,talk,be,bgm1,bgm2
    game_framework.reset_time()
    bgm1=load_music('boss.mp3')
    bgm1.set_volume(64)
    bgm1.play()
    bgm2 = load_music('talk.mp3')
    bgm2.set_volume(64)

    nom=load_image('NOM.png')
    image=load_image('boss.png')
    talk=load_image("talking.png")
    be=load_image("bossba.png")
    pass


def exit():
    global image,nom,talk,be,bgm1,bgm2,i,z
    del(image)
    del (nom)
    del (talk)
    del(be)
    del (bgm1)
    del (bgm2)
    i=0
    z=0

    pass


def update(frame_time):
    global i,z
    i+=1
    if i==5:
        game_framework.change_state(playboss)
    if(z<3):
        z+=1

    delay(2.5)

    pass

def draw(frame_time):
    clear_canvas()
    be.draw(400,300)
    image.clip_draw(0, 0, 200, 160, 500, 350)
    nom.draw(70,70)
    talk.clip_draw(0,i*100,100,100,650,450)
    talk.clip_draw(100,i*100,100,100,150,180)
    if (z >= 2):
        bgm2.play()
    update_canvas()
    pass





def handle_events(frame_time):
    pass


def pause(): pass


def resume(): pass



