from model import Cat, Cube, Object


class ObjectFactory:

    def __init__(self, app):
        self.app = app

    def create_cat(self, **kwargs):
        return Cat(self.app, **kwargs)

    def create_cube(self, **kwargs):
        return Cube(self.app, **kwargs)

    def create_object(self, scale, **kwargs):
        return Object(self.app, vao_name='mountain', scale=scale, **kwargs)
