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
        self.__facade = GameFacade(self)

    def run(self):
        while True:
            self.__get_time()
            self.__check_events()
            self.__facade.camera.update()
            self.__render()
            self.__facade.delta_time = self.clock.tick(60)





    def __get_time(self):
        self.__facade.time = pg.time.get_ticks() * 0.001

    def __check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.__facade.mesh.destroy()
                self.__facade.scene.destroy()
                pg.quit()
                sys.exit()

    def __render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18, 1))
        self.__facade.scene.render()
        pg.display.flip()



if __name__ == '__main__':
    app = GameEngine()
    app.run()
