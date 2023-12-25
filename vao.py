from vbo import VBO
from shader_program import ShderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShderProgram(ctx)
        self.vaos = {}

        self.vaos['cube'] = self.get_vao()

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attibs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
