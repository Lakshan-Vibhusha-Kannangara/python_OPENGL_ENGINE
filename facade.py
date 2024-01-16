from camera import Camera
from light import Light
from mesh import Mesh
from object_factory import ObjectFactory
from scene import Scene


class GameFacade:
    def __init__(self, app):
        self.ctx = app.ctx
        self.WIN_SIZE = (1600, 900)
        self.time = 0
        self.delta_time = 0
        self.light = Light()
        self.camera = Camera(self)
        self.mesh = Mesh(self)
        self.__object_factory = ObjectFactory(self)
        self.scene = Scene(self.__object_factory)
