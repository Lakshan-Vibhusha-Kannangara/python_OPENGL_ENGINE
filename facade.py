from camera import Camera
from light import Light
from mesh import Mesh
from object_factory import ObjectFactory
from scene import Scene
from texture import Texture
from vao import VAO
from vbo import VBO


class GameFacade:
    def __init__(self, app):
        self.ctx = app.ctx
        self.WIN_SIZE = (1600, 900)
        self.time = 0
        self.delta_time = 0
        self.light = Light()
        self.camera = Camera(self)
        self.vbo = VBO(self.ctx)
        self.vao = VAO(self.ctx, self.vbo)
        self.texture = Texture(self.ctx)
        self.mesh = Mesh(self, self.vao, self.texture)
        self.__object_factory = ObjectFactory(self, self.vao, self.texture, self.vbo)
        self.scene = Scene(self.__object_factory)
