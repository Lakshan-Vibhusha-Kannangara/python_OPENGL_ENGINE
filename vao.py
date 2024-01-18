from shader_program import ShaderProgram
from vbo import VBO


class VAO:
    def __init__(self, ctx,vbo):
        self.ctx = ctx
        self.vbo = vbo
        self.vaos = {}
        self.__program = ShaderProgram(ctx)
        self.setup_vao('cube', 'default')
        self.setup_vao('skybox', 'skybox')


    def destroy(self):
        self.vbo.destroy()
        self.__program.destroy()
        for vao in self.vaos.values():
            vao.release()

    def __setup_vaos_from_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('#'):
                    continue

                name, _, _ = line.strip().split()
                self.setup_vao(name, 'default')

    def setup_vao(self, vbo_name, program_name):
        if vbo_name not in self.vbo.vbos:
            # Handle the case where vbo_name is not found
            print(f"VBO with name '{vbo_name}' not found.")
            return None

        vbo = self.vbo.vbos[vbo_name]
        program = self.__program.programs[program_name]
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        self.vaos[vbo_name] = vao
        return vao


