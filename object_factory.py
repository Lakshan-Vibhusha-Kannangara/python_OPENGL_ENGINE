from model import Cat, Cube, Object


class ObjectFactory:

    def __init__(self, app, vao, texture, vbo):
        self.app = app
        self.vao = vao
        self.texture = texture
        self.vbo = vbo

    def create_cat(self, **kwargs) -> Cat:
        return Cat(self.app, **kwargs)

    def create_cube(self, **kwargs) -> Cube:
        return Cube(self.app, **kwargs)

    def create_object(self, vao_name, tex_id, scale, obj_path, tex_path, pos, **kwargs) -> Object:

        self.texture.textures[tex_id] = self.texture.get_texture(path=tex_path)

        vbo = self.vbo.load_objects_from_obj(self.app.ctx, vao_name, obj_path, tex_path)

        if vao_name not in self.app.mesh.vao.vaos:
            self.vao.vaos[vao_name] = self.vao.setup_vao(vao_name, 'default')

        if vao_name in self.vao.vaos:
            self.vbo.vbos[vao_name] = vbo

            return Object(self.app, vao_name=vao_name, tex_id=tex_id, scale=scale, pos=pos, **kwargs)
        else:
            print(f"Vao with name '{vao_name}' not found.")
