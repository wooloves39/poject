import game_framework
from pico2d import *
import main_game
import math
name = "StartState"
logo_time = 0.0

clear=None
be=None
def enter():
    import os
    os.chdir('D:/2016/2d gp/project/image')
    global be,clear
    game_framework.reset_time()
    be=load_image("bossba.png")
    clear=load_image("clear.png")
    pass
def exit():
    global be,clear
    del(be)
    del(clear)
    pass
def update(frame_time):
    pass
def draw(frame_time):
    clear_canvas()
    be.draw(400,300)
    clear.draw(300,300)
    update_canvas()
    pass
def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
    pass
def pause(): pass
def resume(): pass