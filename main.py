from ursina import *

app = Ursina()
window.title = "Pyxinhos"

Sky()

margin = Entity(
    model="cube",
    color=color.green,
    scale=(100, 1, 40),
    position=(0,0, -15),
)

water = Entity(
    moodel="plane",
    color=color.azure,
    scale=(100, 1, 40),
    position=(0, 0, -15),
)

deck = Entity(
    model="cube",
    color=color.brown,
    scale=(3, 0.3, 10),
    position=(0, 0.85, 4),
)

class Jogador(Entity):
    def __init__(self):
        super().__init__(position=(0, 2.5, 0))
        camera.parent = self
        camera.position = (0, 0, 0)
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        self.sensibilidade = 40
        mouse.locked = True

    def update(self):
        self.rotation_y += mouse.velocity[0] * self.sensibilidade
        camera.rotation_x -= mouse.velocity[1] * self.sensibilidade
        camera.rotation_x = clamp(camera.rotation_x, -80, 80)


jogador = Jogador()


def input(key):
    if key == "escape":
        application.quit()


app.run()