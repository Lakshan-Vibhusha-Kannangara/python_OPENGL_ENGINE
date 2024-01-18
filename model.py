import numpy as np
import glm
import pygame as pg


class BaseModel:

    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self._app = app
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self._app.camera
        self._pos = pos
        self._scale = scale
        self.__rot = glm.vec3([glm.radians(a) for a in rot])
        self._m_model = self._get_model_matrix()
        self._tex_id = tex_id

    def render(self) -> None:
        self.update()
        self.vao.render()

    def update(self) -> None:
        pass

    def _get_model_matrix(self):
        m_model = glm.mat4()
        m_model = glm.translate(m_model, self._pos)
        m_model = glm.rotate(m_model, self.__rot.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.__rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.__rot.z, glm.vec3(0, 0, 1))
        m_model = glm.scale(m_model, self._scale)
        return m_model


class ExtendedBaseModel(BaseModel):

    def __init__(self, app, vao_name, tex_id, pos, rot, scale):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self._on_init()

    def update(self) -> None:
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self._m_model)

    def _on_init(self):
        self.texture = self._app.mesh.texture.textures[self._tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()

        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self._m_model)

        self.program['light.position'].write(self._app.light.position)
        self.program['light.Ia'].write(self._app.light.Ia)
        self.program['light.Id'].write(self._app.light.Id)
        self.program['light.Is'].write(self._app.light.Is)

        # Use create_vao method to create a new VAO for each cube

    def destroy(self):
        pass


class Cube(ExtendedBaseModel):

    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class Cat(ExtendedBaseModel):

    def __init__(self, app, vao_name='cat', tex_id='cat', pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class Object(ExtendedBaseModel):

    def __init__(self, app, tex_id, vao_name, pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class SkyBox(BaseModel):

    def __init__(self, app, vao_name='skybox', tex_id='skybox', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self._on_init()

    def update(self) -> None:
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))

    def _on_init(self):
        # texture
        self.texture = self._app.mesh.texture.textures[self._tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)

        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))
