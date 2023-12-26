from shader_program import ShderProgram
from vbo import VBO


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShderProgram(ctx)
        self.vaos = {}

        self.vaos['cube'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['cube'])

        self.vaos['cat'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['cat'])
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def create_vao(self, vbo_name, program_name):
        vbo = self.vbo.vbos[vbo_name]
        program = self.program.programs[program_name]
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
