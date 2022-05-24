import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

arestas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)


cores = (
    ((1,1,1)),
    ((0.8,0.5,1)),
    ((1,0.7,0)),
    ((0.4,0.1,0.8)),
    ((0.3,0,1)),
    ((0,0.5,1)),
    ((0,0.7,1)),
    ((0.2,0.5,0)),
    
)

def Cube():

    glBegin(GL_LINES)
    for aresta in arestas:
        for vertice in aresta:
            glVertex3fv(vertices[vertice])
    glEnd()
    
    glBegin(GL_QUADS)
    for face in range(len(faces)):
        for vertice in range(len(faces[face])):
            glVertex3fv(vertices[faces[face][vertice]])
            glColor3fv(cores[vertice])
            
    glEnd()

    
def interagirTeclado(event_key):
    
    if(event_key == pygame.K_UP):
        glRotatef(-8.0, 8.0, 0.0, 0.0)
    elif(event_key == pygame.K_DOWN):
        glRotatef(8.0, 8.0, 0.0, 0.0)
    elif(event_key == pygame.K_LEFT):
        glRotatef(-8.0, 0.0, 8.0, 0.0)
    elif(event_key == pygame.K_RIGHT):
        glRotatef(8.0, 0.0, 8.0, 0.0)

def main():

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:

                interagirTeclado(event.key)
                
        #glRotatef(1, 1, 3, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()