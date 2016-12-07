import game_framework
import title
import playboss
import platform
import os
if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

from pico2d import *
open_canvas()
game_framework.run(title)
close_canvas()
