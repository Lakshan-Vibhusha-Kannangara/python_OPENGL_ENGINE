from shader_program import ShaderProgram
from vbo import VBO


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}
        self.setup_vao('cube', 'default')
        self.setup_vao('skybox', 'skybox')
        self.setup_vaos_from_file('objects.txt')

    def setup_vaos_from_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('#'):
                    continue

                name, _, _ = line.strip().split()
                self.setup_vao(name, 'default')

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
        for vao in self.vaos.values():
            vao.release()

        self.setup_vao('cat', 'default')

    def setup_vao(self, vbo_name, program_name):
        vbo = self.vbo.vbos[vbo_name]
        program = self.program.programs[program_name]
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        self.vaos[vbo_name] = vao

    def create_vao(self, vbo_name, program_name):
        vbo = self.vbo.vbos[vbo_name]
        program = self.program.programs[program_name]
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
        for vao in self.vaos.values():
            vao.release()
