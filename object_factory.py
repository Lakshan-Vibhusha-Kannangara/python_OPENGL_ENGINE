from model import Cat, Cube, Object


class ObjectFactory:

    def __init__(self, app):
        self.app = app

    def create_cat(self, **kwargs) -> Cat:
        return Cat(self.app, **kwargs)

    def create_cube(self, **kwargs) -> Cube:
        return Cube(self.app, **kwargs)

    def create_object(self, vao_name, tex_id, scale, tex_path, pos, **kwargs) -> Object:
        self.app.mesh.texture.textures[tex_id] = self.app.mesh.texture.get_texture(
            path=tex_path)

        return Object(self.app, vao_name=vao_name, tex_id=tex_id, scale=scale, pos=pos, **kwargs)
