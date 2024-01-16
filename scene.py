from model import *


class Scene:
    def __init__(self, object_factory):

        self.__objects = []
        self.__load(object_factory)
        self.__skybox = SkyBox(object_factory.app)

    def render(self):
        for obj in self.__objects:
            obj.render()
        self.__skybox.render()

    def destroy(self):
        pass

    def __load(self, object_factory):

        add = self.__add_object

        add(object_factory.create_cat(pos=(0, -2, -10)))
        n, s = 30, 3
        add(object_factory.create_object(scale=(0.1, 0.1, 0.1), pos=(0, 10, -10)))

        for x in range(-n, n, s):
            for z in range(-n, n, s):
                pass
                add(object_factory.create_cube(pos=(x, -s, z)))

    def __add_object(self, obj):
        self.__objects.append(obj)
