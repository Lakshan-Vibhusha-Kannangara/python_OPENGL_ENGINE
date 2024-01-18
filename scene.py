from model import *
from object_factory import ObjectFactory


class Scene:
    def __init__(self, object_factory: ObjectFactory):
        self.__objects = []
        self.__load(object_factory)
        self.__skybox = SkyBox(object_factory.app)

    def render(self) -> None:
        for obj in self.__objects:
            obj.render()
        self.__skybox.render()

    def destroy(self):
        pass

    def __load(self, object_factory):

        add = self.__add_object

        #add(object_factory.create_cat(pos=(0, -2, -10)))
        n, s = 30, 3

        add(object_factory.create_object(vao_name='horse', tex_id='horse',obj_path='objects/horse/10026_Horse_v01-it2.obj',
                                         tex_path='objects/horse/Horse_v01.jpg',
                                         scale=(0.001, 0.001, 0.001), pos=(0, -1, 0)))

        add(object_factory.create_object(vao_name='grass', tex_id='grass',obj_path='objects/grass/10450_Rectangular_Grass_Patch_v1_iterations-2.obj',
                                         tex_path='objects/grass/10450_Rectangular_Grass_Patch_v1_Diffuse.jpg',
                                         scale=(1, 1, 1), pos=(0, -9, 0)))
       # for x in range(-n, n, s):
           # for z in range(-n, n, s):
             #   pass
              #  add(object_factory.create_cube(pos=(x, -s, z)))

    def __add_object(self, obj):
        self.__objects.append(obj)
