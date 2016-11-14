import game_framework
from pico2d import *
import main_game
name = "StartState"
image = None
logo_time = 0.0
nom=None
font = None

def enter():
    import os
    os.chdir('D:/2016/2d gp/project/image')
    global image,nom,font
    nom=load_image('NOM.png')
    image=load_image('boss.png')
    font = load_font('ENCR10B.TTF', 30)
    pass


def exit():
    global image,nom,font
    del(image)
    del (nom)
    del (font)
    pass


def update():
    pass


def draw():
    clear_canvas()
    image.clip_draw(0,0, 200, 160, 500, 350)
    nom.draw(70,70)
    font.draw(500, 480, 'But the neoneuntoe waedasi to appear!!')
    font.draw(70, 150, 'So I am going to make me regret my.', (128, 128, 128))
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



