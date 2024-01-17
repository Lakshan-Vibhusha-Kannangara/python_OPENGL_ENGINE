from vao import VAO
from texture import Texture


class Mesh:

    #####if you changed the mesh file implementation you can load any data file as you want#########
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.ctx)
        self.texture = Texture(app.ctx)

    def destroy(self) -> None:
        self.vao.destroy()
        self.texture.destroy()
