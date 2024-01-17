from shader_program import ShaderProgram
from vbo import VBO


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vaos = {}
        self.__vbo = VBO(ctx)
        self.__program = ShaderProgram(ctx)
        self.__setup_vao('cube', 'default')
        self.__setup_vao('skybox', 'skybox')
        self.__setup_vaos_from_file('objects.txt')

    def destroy(self):
        self.__vbo.destroy()
        self.__program.destroy()
        for vao in self.vaos.values():
            vao.release()

        self.__setup_vao('cat', 'default')

    def __setup_vaos_from_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('#'):
                    continue

                name, _, _ = line.strip().split()
                self.__setup_vao(name, 'default')

    def __setup_vao(self, vbo_name, program_name):
        vbo = self.__vbo.vbos[vbo_name]
        program = self.__program.programs[program_name]
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        self.vaos[vbo_name] = vao

    def __create_vao(self, vbo_name, program_name):
        vbo = self.__vbo.vbos[vbo_name]
        program = self.__program.programs[program_name]
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao
