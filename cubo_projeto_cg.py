import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
( 1, -1, -1),
( 1,  1, -1),
(-1,  1, -1),
(-1, -1, -1),
( 1, -1,  1),
( 1,  1,  1),
(-1, -1,  1),
(-1,  1,  1),
)

coordenadasDeTextura = ((0, 0), (0, 1), (1, 1), (1, 0))

faces = (
(0,1,2,3),
(3,2,7,6),
(6,7,5,4),
(4,5,1,0),
(1,5,7,2),
(4,0,3,6),
)

normals = [
( 0,  0, -1),
(-1,  0,  0),
( 0,  0,  1),
( 1,  0,  0),
( 0,  1,  0),
( 0, -1,  0) 
    ]

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
(5,7),
)


def Cubo():
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    for i_face, face in enumerate(faces):
        glNormal3fv(normals[i_face])

        
        for i_vertice, vertice in enumerate(face):
            
            glTexCoord2fv(coordenadasDeTextura[i_vertice])
            glVertex3fv(vertices[vertice])
        
            
    glEnd()

    glColor3fv((0,0,0))
    glBegin(GL_LINES)
    for aresta in arestas:
        for vertice in aresta:
            glVertex3fv(vertices[vertice])
    glEnd()


def interagirTeclado(event_key, movimento):
    
    if(event_key == pygame.K_UP):
        glRotatef(-movimento, movimento, 0.0, 0.0)
    elif(event_key == pygame.K_DOWN):
        glRotatef(movimento, movimento, 0.0, 0.0)
    elif(event_key == pygame.K_LEFT):
        glRotatef(-movimento, 0.0, movimento, 0.0)
    elif(event_key == pygame.K_RIGHT):
        glRotatef(movimento, 0.0, movimento, 0.0)


def aplicarTextura(img):
    imagem = pygame.image.load(img)
    dados = pygame.image.tostring(imagem, 'RGBA')

    imagem_tex = glGenTextures(1)
    
    glBindTexture(GL_TEXTURE_2D, imagem_tex)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, imagem.get_width(), imagem.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, dados)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glEnable(GL_TEXTURE_2D)

def main():
    global faces

    pygame.init()
    display = (1024, 1024)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -6)

    glLight(GL_LIGHT0, GL_POSITION,  (-2, -4, 5, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST) 

    aplicarTextura("Images/zebrinha.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  
            if event.type == pygame.KEYDOWN:
                
                interagirTeclado(event.key, 10)    

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )

        Cubo()

        pygame.display.flip()
        clock.tick(60)

main()