import game_framework
from pico2d import *
import main_game
name = "StartState"
image = None
logo_time = 0.0
nom=None
talk=None
i=0
def enter():
    import os
    os.chdir('D:/2016/2d gp/project/image')
    global image,nom,talk
    nom=load_image('NOM.png')
    image=load_image('boss.png')
    talk=load_image("talking.png")
    pass


def exit():
    global image,nom,talk
    del(image)
    del (nom)
    del (talk)
    pass


def update():
    global i
    i+=1

    pass


def draw():
    clear_canvas()
    image.clip_draw(0,0, 200, 160, 500, 350)
    nom.draw(70,70)
    talk.clip_draw(0,i*100,100,100,650,450)
    talk.clip_draw(100,i*100,100,100,150,180)
    update_canvas()
    delay(3)
    pass





def handle_events():
    pass


def pause(): pass


def resume(): pass



