import numpy as np
import OpenGL.GL as gl
from PIL import Image

texture_id = None

def draw_figure(vertices_figure, tipo_figura):
    gl.glBegin(tipo_figura)
    for x, y, z in vertices_figure:
        # Coordenadas de textura
        gl.glVertex3f(x, y, z)
    gl.glEnd()


def measures():
    eixo_X = [(-3.0, 0.0, 0.0), (3.0, 0.0, 0.0)]
    eixo_Y = [(0.0, -3.0, 0.0), (0.0, 3.0, 0.0)]
    eixo_Z = [(0.0, 0.0, -3.0), (0.0, 0.0, 3.0)]

    gl.glColor3f(1.0, 0.0, 0.0)
    draw_figure(eixo_X, gl.GL_LINES)
    gl.glColor3f(0.0, 1.0, 0.0)
    draw_figure(eixo_Y, gl.GL_LINES)
    gl.glColor3f(0.0, 0.0, 1.0)
    draw_figure(eixo_Z, gl.GL_LINES)


def draw_pillar():
    pillar= [
        # Posições             # Coordenadas de textura
        (0.0, 0.0, 0.0, 0.0, 0.0), (0.2, 0.0, 0.0, 1.0, 0.0), 
        (0.2, 0.0, 0.2, 1.0, 1.0), (0.0, 0.0, 0.2, 0.0, 1.0),
        (0.0, 0.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 1.0, 0.0),
        (0.2, 1.0, 0.0, 1.0, 1.0), (0.2, 0.0, 0.0, 0.0, 1.0),
        (0.2, 0.0, 0.0, 0.0, 0.0), (0.2, 1.0, 0.0, 1.0, 0.0),
        (0.2, 1.0, 0.2, 1.0, 1.0), (0.2, 0.0, 0.2, 0.0, 1.0),
        (0.2, 0.0, 0.2, 0.0, 0.0), (0.2, 1.0, 0.2, 1.0, 0.0),
        (0.0, 1.0, 0.2, 1.0, 1.0), (0.0, 0.0, 0.2, 0.0, 1.0),
        (0.0, 0.0, 0.2, 0.0, 0.0), (0.0, 1.0, 0.2, 1.0, 0.0),
        (0.0, 1.0, 0.0, 1.0, 1.0), (0.0, 0.0, 0.0, 0.0, 1.0),
        (0.0, 1.0, 0.0, 1.0, 1.0), (0.2, 1.0, 0.0, 1.0, 0.0),
        (0.2, 1.0, 0.2, 1.0, 1.0), (0.0, 1.0, 0.2, 0.0, 1.0)
    ]


    #ativa a textura
    gl.glActiveTexture(gl.GL_TEXTURE0)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id) #aplicando a textura
    gl.glColor3f(139, 69, 19)  #marrom

    gl.glBegin(gl.GL_QUADS)
    for x, y, z, s, t in pillar:
        gl.glTexCoord2f(s, t)  # Coordenadas de textura
        gl.glVertex3f(x, y, z)
    gl.glEnd()
    
   


def draw_table(): #falta texturizar
    #topo
    gl.glPushMatrix()
    gl.glTranslatef(0, 0.5, 0)
    gl.glScalef(10, 0.5, 1)
    gl.glRotatef(270, 1, 0, 0)
    draw_pillar()
    gl.glPopMatrix()

    #bancos
    gl.glPushMatrix()
    gl.glTranslatef(0, 0.2, -1)
    gl.glScalef(10, 0.2, 0.15)
    gl.glRotatef(270, 1, 0, 0)
    draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(0, 0.2, 0.1)
    gl.glScalef(10, 0.2, 0.15)
    gl.glRotatef(270, 1, 0, 0)
    draw_pillar()
    gl.glPopMatrix()

    #pernas
    gl.glPushMatrix()
    gl.glTranslatef(0.15, 0, -0.1)
    gl.glScalef(0.6, 0.5, 0.3)
    draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(0.15, 0, -1)
    gl.glScalef(0.6, 0.5, 0.3)
    draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(1.65, 0, -0.1)
    gl.glScalef(0.6, 0.5, 0.3)
    draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(1.65, 0, -1)
    gl.glScalef(0.6, 0.5, 0.3)
    draw_pillar()
    gl.glPopMatrix()

    #apoio de baixo
    gl.glPushMatrix()
    gl.glTranslatef(0.15, 0, 0)
    gl.glScalef(0.6, 0.3, 1.05)
    gl.glRotatef(270, 1, 0, 0)
    draw_pillar()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(1.65, 0, 0)
    gl.glScalef(0.6, 0.3, 1.05)
    gl.glRotatef(270, 1, 0, 0)
    draw_pillar()
    gl.glPopMatrix()

def draw_roof():

    # Coordenadas dos vértices e coordenadas de textura
    lado_esquerdo = [
        (-2.0, 0.0, 2.0, 0.0, 2.0),  #top right
        (0.0, 2.0, 2.0, 2.0, 2.0),  #bottom right
        (0.0, 2.0, -2.0, 2.0, 0.0),  #bottom left
        (-2.0, 0.0, -2.0, 0.0, 0.0)  #top left
    ]
    lado_direito = [
        (2.0, 0.0, 2.0, 0.0, 2.0),
        (0.0, 2.0, 2.0, 2.0, 2.0),
        (0.0, 2.0, -2.0, 2.0, 0.0), 
        (2.0, 0.0, -2.0, 0.0, 0.0)
    ]

    # Ativar a textura
    gl.glActiveTexture(gl.GL_TEXTURE0)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glColor3f(139, 69, 19)  #marrom

    gl.glBegin(gl.GL_QUADS)
    for x, y, z, s, t in lado_esquerdo:
        gl.glTexCoord2f(s, t)  # Coordenadas de textura
        gl.glVertex3f(x, y, z)
    gl.glEnd()

    gl.glBegin(gl.GL_QUADS)
    for x, y, z, s, t in lado_direito:
        gl.glTexCoord2f(s, t)  # Coordenadas de textura
        gl.glVertex3f(x, y, z)
    gl.glEnd()


def draw_floor():

    vertices_piso = [
        # Posições (x, y, z)          # Coordenadas de textura (s, t)
        (-2.0, 0.0, -2.0, 0.0, 0.0),  # Inferior esquerdo
        (2.0, 0.0, -2.0, 5.0, 0.0),  # Inferior direito
        (2.0, 0.0, 2.0, 5.0, 2.0),  # Superior direito
        (-2.0, 0.0, 2.0, 0.0, 2.0)  # Superior esquerdo
    ]

    # Ativar a textura
    gl.glActiveTexture(gl.GL_TEXTURE0)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glColor3f(139, 69, 19)  #marrom

    gl.glBegin(gl.GL_QUADS)
    for x, y, z, s, t in vertices_piso:
        gl.glTexCoord2f(s, t)  # Coordenadas de textura
        gl.glVertex3f(x, y, z)
    gl.glEnd()


def load_texture(image_path):
    global texture_id
    texture_id = gl.glGenTextures(1) #identificador da textura
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    try:
        image = Image.open(image_path)
        image = image.convert('RGBA')
        image = image.rotate(90, expand=True)
        img_data = np.array(image)


        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, image.width,
                        image.height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE,
                        img_data)

        
        # Define os parametros de textura: como a textura vai se comportar.
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S,
                           gl.GL_MIRRORED_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T,
                           gl.GL_MIRRORED_REPEAT)
        
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER,
                           gl.GL_LINEAR) #interpolação linear é mais suave
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER,
                           gl.GL_LINEAR)

    except Exception as e:
        print(f"Error loading texture: {e}")
