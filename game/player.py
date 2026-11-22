from ursina import *


class Player(Entity):
    def __init__(self):
        super().__init__(position=(0, 2.5, 0))
        camera.parent = self
        camera.position = (0, 0, 0)
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        self.sensibilidade = 40
        self.limite_horizontal = 70
        self.limite_vertical = 80
        mouse.locked = True

    def update(self):
        self.rotation_y += mouse.velocity[0] * self.sensibilidade
        self.rotation_y = clamp(
            self.rotation_y, -self.limite_horizontal, self.limite_horizontal
        )

        camera.rotation_x -= mouse.velocity[1] * self.sensibilidade
        camera.rotation_x = clamp(
            camera.rotation_x, -self.limite_vertical, self.limite_vertical
        )