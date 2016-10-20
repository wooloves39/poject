import game_framework
from pico2d import *
import main_game
name = "StartState"
image = None
logo_time = 0.0


def enter():
    import os
    os.chdir('D:/2016/2d gp/project/image')
    global image

    image=load_image('start.png')
    pass


def exit():
    global image
    del(image)

    pass


def update():
    pass


def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass





def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type)==(SDL_KEYDOWN)and (event.key)!=(SDLK_ESCAPE):
                game_framework.change_state(main_game)
    pass


def pause(): pass


def resume(): pass




