import glm
import pygame as pg

FOV = 50
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSITIVITY = 0.05


class Camera:
    def __init__(self, app, position=(0, 0, 4), yaw=-90, pitch=0):
        self.__up = glm.vec3(0, 1, 0)
        self.__right = glm.vec3(1, 0, 0)
        self.__forward = glm.vec3(0, 0, -1)

        self.app = app
        self.aspect_ratio = self.app.WIN_SIZE[0] / self.app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.m_view = self.__get_view_matrix()
        self.m_proj = self.__get_projection_matrix()
        self.__yaw = yaw
        self.__pitch = pitch
        self.__observers = []

    def update(self):
        self.__move()
        self.__rotate()
        self.__update_camera_vectors()
        self.m_view = self.__get_view_matrix()
        self.__update_observers()

    def __attach(self, observer):
        self.__observers.append(observer)

    def __update_observers(self):
        for observer in self.__observers:
            observer.update()

    def __rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.__yaw += rel_x * SENSITIVITY
        self.__pitch -= rel_y * SENSITIVITY
        self.__pitch = max(-89, min(89, self.__pitch))

    def __update_camera_vectors(self):
        yaw, pitch = glm.radians(self.__yaw), glm.radians(self.__pitch)

        self.__forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.__forward.y = glm.sin(pitch)
        self.__forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.__forward = glm.normalize(self.__forward)
        self.__right = glm.normalize(glm.cross(self.__forward, glm.vec3(0, 1, 0)))
        self.__up = glm.normalize(glm.cross(self.__right, self.__forward))

    def __move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.position += self.__forward * velocity

        if keys[pg.K_s]:
            self.position -= self.__forward * velocity

        if keys[pg.K_a]:
            self.position -= self.__right * velocity

        if keys[pg.K_d]:
            self.position += self.__right * velocity

        if keys[pg.K_q]:
            self.position += self.__up * velocity

        if keys[pg.K_e]:
            self.position -= self.__up * velocity

    def __get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)

    def __get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.__forward, self.__up)

    def __get_model_matrix(self):
        m_model = glm.mat4()
        return m_model
