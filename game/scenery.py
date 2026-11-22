from ursina import *


def generate_scenery():
    Sky()

    margin = Entity(
        model="cube",
        color=color.green,
        scale=(100, 1, 40),
        position=(0, 0, -15),
    )

    water = Entity(
        model="plane",
        color=color.azure,
        scale=(100, 1, 100),
        position=(0, 0.3, 55),
    )

    deck = Entity(
        model="cube",
        color=color.brown,
        scale=(3, 0.3, 10),
        position=(0, 0.85, 4),
    )

    return margin, water, deck