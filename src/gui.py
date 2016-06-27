import pyglet
from pyglet.gl import *
from OpenGL.GLUT import *


class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)

    def on_draw(self):
        # super(MainWindow, self).on_draw()
        # self.clear()
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glBegin(GL_TRIANGLES)
        glVertex2f(0, 0)
        glVertex2f(self.width, 0)
        glVertex2f(self.width, self.height)
        glEnd()
