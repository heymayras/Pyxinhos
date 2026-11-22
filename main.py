from ursina import *

from game.scenery import generate_scenery
from game.player import Player

app = Ursina()
window.title = "Pyxinhos"

scenery = generate_scenery()
player = Player()


def input(key):
    if key == "escape":
        application.quit()


app.run()