from model import *


class Scene:
    def __init__(self,  object_factory):

        self.objects = []
        self.load(object_factory)
        self.skybox = SkyBox(object_factory.app)

    def load(self, object_factory):

        add = self.add_object

        add(object_factory.create_cat(pos=(0, -2, -10)))
        n, s = 30, 3
        add(object_factory.create_object(scale=(0.1,0.1,0.1),pos=(0, 10, -10)))

        for x in range(-n, n, s):
            for z in range(-n, n, s):
                pass
                add(object_factory.create_cube(pos=(x, -s, z)))

    def add_object(self, obj):
        self.objects.append(obj)

    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()

    def destroy(self):
        pass
