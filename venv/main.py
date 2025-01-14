import sys

import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

import functions

# Constantes e variáveis globais
SPEED_CAMERA = 0.05  # Velocidade com que a câmera se desloca

aspecto = 1.0  # Razão atual da largura e altura da janela

CamX = 1.0  # Posição atual da câmera (x)
CamY = 1.0  # Posição atual da câmera (y)
CamZ = 1.0  # Posição atual da câmera (z)

RotatAngulo = 0.0  # Ângulo de rotação do objeto
TransPosX = 0.0  # Posição de translação do objeto ao longo do eixo X
TransPosZ = 0.0  # Posição de translação do objeto ao longo do eixo Z
ScaleEixos = 1.0  # Fator de escala do objeto


def confCamera():
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(60.0, 1.0, 0.1, 100.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    glu.gluLookAt(
        CamX,
        CamY,
        CamZ,  # Posição da câmera
        0,
        0,
        0,  # Ponto para onde a câmera está olhando (centro da cena)
        0,
        1,
        0  # Vetor "para cima" (direção do eixo Y)
    )


def keyboard(key, x, y):
    """Função responsável por eventos de teclado."""
    global CamX, CamY, CamZ, RotatAngulo, TransPosX, TransPosZ, ScaleEixos
    match key:
        case b'\x1b':  # ESC key
            sys.exit()  # Encerra o programa

        case b'X':
            CamX += SPEED_CAMERA  # esquerda
        case b'x':
            CamX -= SPEED_CAMERA  # direita
        case b'Y':
            CamY += SPEED_CAMERA  # cimaa
        case b'y':
            CamY -= SPEED_CAMERA  # baixo
        case b'Z':
            CamZ += SPEED_CAMERA  # aproximar
        case b'z':
            CamZ -= SPEED_CAMERA  # afastar

        case b'R':
            RotatAngulo += 1.0  # Aumenta o ângulo de rotação
        case b'r':
            RotatAngulo -= 1.0  # Diminui o Xângulo de rotação

        case b'd':
            TransPosX -= 0.1  # Aumenta a posição de translação ao longo do eixo X
        case b'a':
            TransPosX += 0.1  # Diminui a posição de translação ao longo do eixo X
        case b'w':
            TransPosZ += 0.1  # Aumenta a posição de translação ao longo do eixo Z
        case b's':
            TransPosZ -= 0.1  # Diminui a posição de translação ao longo do eixo Z

        case b'E':
            ScaleEixos += 0.1  # Aumenta a escala
        case b'e':
            ScaleEixos -= 0.1  # Diminui a escala

    # Atualiza a tela após as modificações
    glut.glutPostRedisplay()


def display():
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glEnable(gl.GL_TEXTURE_2D)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glLoadIdentity()

    confCamera()

    # Aplicar transformações
    gl.glTranslatef(TransPosX, 0, TransPosZ)
    gl.glRotatef(RotatAngulo, 1, 0, 0)
    gl.glScalef(ScaleEixos, ScaleEixos, ScaleEixos)

    functions.measures()

    #piso
    gl.glPushMatrix()
    gl.glTranslatef(0, 0, 0)
    gl.glScalef(1, 0.5, 1)
    functions.load_texture("./image/chao.jpg")
    functions.draw_floor()
    gl.glPopMatrix()

    #mesa
    functions.load_texture("./image/madeira.jpg")

    #mesas
    gl.glPushMatrix()
    gl.glTranslatef(-0.8, 0, 0)
    gl.glScalef(0.8, 0.8, 0.8)
    gl.glRotatef(90, 0, 1, 0)
    gl.glColor3f(0.65, 0.2, 0.2) #brown
    functions.draw_table()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(-0.8, 0, 1.8)
    gl.glScalef(0.8, 0.8, 0.8)
    gl.glRotatef(90, 0, 1, 0)
    functions.draw_table()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(1.6, 0, 0)
    gl.glScalef(0.8, 0.8, 0.8)
    gl.glRotatef(90, 0, 1, 0)
    functions.draw_table()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(1.6, 0, 1.8)
    gl.glScalef(0.8, 0.8, 0.8)
    gl.glRotatef(90, 0, 1, 0)
    functions.draw_table()
    gl.glPopMatrix()
    

    #pilares
    #fila da esquerda
    gl.glPushMatrix()
    gl.glTranslatef(-2, 0, 1.8)
    gl.glScalef(1, 1.5, 1)
    gl.glColor3f(139, 69, 19)  #marrom
    functions.load_texture("./image/coluna.jpeg")
    functions.draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(-2, 0, 0.8)
    gl.glScalef(1, 1.5, 1)
    functions.draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(-2, 0, -1)
    gl.glScalef(1, 1.5, 1)
    functions.draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(-2, 0, -2)
    gl.glScalef(1, 1.5, 1)
    functions.draw_pillar()
    gl.glPopMatrix()

    #fila do meio
    gl.glPushMatrix()
    gl.glTranslatef(-0.1, 0, 1.8)
    gl.glScalef(1, 1.65, 1)
    functions.draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(-0.1, 0, 0.8)
    gl.glScalef(1, 1.65, 1)
    functions.draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(-0.1, 0, -1)
    gl.glScalef(1, 1.65, 1)
    functions.draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(-0.1, 0, -2)
    gl.glScalef(1, 1.65, 1)
    functions.draw_pillar()
    gl.glPopMatrix()

    #fila da direita
    gl.glPushMatrix()
    gl.glTranslatef(1.8, 0, 1.8)
    gl.glScalef(1, 1.5, 1)
    functions.draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(1.8, 0, 0.8)
    gl.glScalef(1, 1.5, 1)
    functions.draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(1.8, 0, -1)
    gl.glScalef(1, 1.5, 1)
    functions.draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(1.8, 0, -2)
    gl.glScalef(1, 1.5, 1)
    functions.draw_pillar()
    gl.glPopMatrix()

    #teto
    gl.glPushMatrix()
    gl.glTranslatef(0, 1.5, 0)
    gl.glScalef(1, 0.5, 1)
    functions.load_texture("./image/originall.jpg")
    functions.draw_roof()
    gl.glPopMatrix()
    
    glut.glutSwapBuffers()


def main():
    # Inicialização do GLUT
    glut.glutInit(sys.argv)
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB
                             | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(800, 600)
    glut.glutCreateWindow("OpenGL Window")

    # Configurações de OpenGL
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)  # Cor de fundo preta

    # Carregar a textura

    # Configurar callbacks
    glut.glutDisplayFunc(display)
    glut.glutKeyboardFunc(keyboard)

    # Configurar a perspectiva e a câmera
    confCamera()

    glut.glutIdleFunc(glut.glutPostRedisplay)

    # Loop principal
    glut.glutMainLoop()


if __name__ == "__main__":
    main()
