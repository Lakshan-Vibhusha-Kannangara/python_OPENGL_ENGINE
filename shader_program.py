class ShaderProgram:
    def __init__(self, ctx):
        self.__ctx = ctx
        self.programs = {'default': self.get_program('default'), 'skybox': self.get_program('skybox')}

    def get_program(self, shader_program_name):
        with open(f'shaders/{shader_program_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_program_name}.frag') as file:
            fragment_shader = file.read()

        program = self.__ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def destroy(self):
        [program.release() for program in self.programs.values()]
