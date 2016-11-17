import game_framework
from pico2d import *
import item
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
from item import attack_item
from item import bonus_item
from boss import Boss
from boss import BossAttack
from nom import Nom
from nom import Life
import title
items=None
boss=None
attack=None
item2=None
def enter():
    import os
    os.chdir('D:/2016/2d gp/project/image')
    global image,nom,talk,be,boss,life,attack,items,item2
    game_framework.reset_time()
    boss=Boss()
    nom=Nom()
    be=load_image("bossba.png")
    attack = [BossAttack() for i in range(12)]
    life=Life()
    items = [attack_item() for i in range(10)]
    item2=bonus_item()
    pass


def exit():
    global nom,be,boss,life,items,item2
    del (nom)
    del(be)
    del (boss)
    del (items)
    pass


def update(frame_time):
    if boss.life <= 0:
        game_framework.change_state(clear)
    else:
        for item in items:
            item.update(frame_time,nom.state)
        item2.update(frame_time,nom.state)
        boss.update(frame_time)
        for item in items:
            if collide(nom,item):
                item.ck=1
            if collide(boss,item):
                items.remove(item)
                boss.life-=1
                pass
        if(item2.sw==0):
            if collide(nom,item2):
                nom.life+=1
                life.switch+=1
                item2.sw=1

        for at in attack:
            at.update(frame_time)
        for at in attack:
            if collide(nom, at):
                boss.ck=1
                attack.remove(at)
                nom.state+=5
                if nom.state>10:
                    nom.state-=5
                nom.frame=0
                nom.life-=1
                life.switch-=1
        nom.update(frame_time)
    pass


def draw(frame_time):
    clear_canvas()
    be.draw(400,300)
    for item in items:
        item.draw()
    item2.draw()
    nom.draw()
    boss.draw()
    for at in attack:
        at.draw()
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
def collide(a, b):
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a>right_b:return False
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False
    return True

    # fill here
    pass


