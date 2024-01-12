import sys
from abstract_engine import BaseGameEngine
from camera import Camera
from facade import GameFacade
from light import Light
from mesh import Mesh
from object_factory import ObjectFactory
from scene import *


class GameEngine(BaseGameEngine):
    def __init__(self, win_size=(1600, 900)):
        super().__init__(win_size)
        self.facade = GameFacade(self)

    def get_time(self):
        self.facade.time = pg.time.get_ticks() * 0.001

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.facade.mesh.destroy()
                self.facade.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18, 1))
        self.facade.scene.render()
        pg.display.flip()

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.facade.camera.update()
            self.render()
            self.facade.delta_time = self.clock.tick(60)


if __name__ == '__main__':
    app = GameEngine()
    app.run()
