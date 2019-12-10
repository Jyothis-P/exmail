from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
def init():
    glClearColor(0.75,0.75,0.75,0.75)
    glOrtho2D(-250.0,250.0,-250.0,250.0)
def lines():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)
    x1=input("Enter x1: ")
    y1=input("Enter y1: ")
    x2=input("Enter x2: ")
    y2=input("Enter y2: ")
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()
    glFlush()
def main():
    glutInit(sys.argv)
    glutInitDisplatMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("test")
    glutDisplayFunc(lines)
    init()
    glutMainLoop()
main()