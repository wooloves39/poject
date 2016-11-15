import game_framework
from pico2d import *
import main_game
import math
name = "StartState"
image = None
logo_time = 0.0
nom=None
talk=None
i=0
be=None
life=None
import clear
from boss import Boss
from nom import Nom
from nom import Life
import title
boss=None
def enter():
    import os
    os.chdir('D:/2016/2d gp/project/image')
    global image,nom,talk,be,boss,life
    game_framework.reset_time()
    boss=Boss()
    nom=Nom()
    be=load_image("bossba.png")
    life=Life()
    pass


def exit():
    global nom,be,boss,life
    del (nom)
    del(be)
    del (boss)
    pass


def update(frame_time):
    boss.update(frame_time)
    nom.update(frame_time)
    boss.life-=1*frame_time
    if boss.life<=0:
        game_framework.change_state(clear)
    pass


def draw(frame_time):
    clear_canvas()
    be.draw(400,300)
    nom.draw()
    boss.draw()
    life.draw()
    update_canvas()
    pass





def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title)
        else:
            nom.handle_event(event)
    pass


def pause(): pass


def resume(): pass



