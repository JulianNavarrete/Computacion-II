from PIL import Image
import numpy as np


def rotarImagen():
    # ubic = str(input("Ingrese el nombre de la imagen con su respectiva extensión: "))
    ubic = "yacht.ppm"
    im = Image.open(ubic)
    alto_img = im.size[0]
    ancho_img = im.size[1]

    matriz_roja_entrada = np.empty((ancho_img, alto_img))
    matriz_verde_entrada = np.empty((ancho_img, alto_img))
    matriz_azul_entrada = np.empty((ancho_img, alto_img))
    matriz_roja_salida = np.empty((alto_img, ancho_img))
    matriz_verde_salida = np.empty((alto_img, ancho_img))
    matriz_azul_salida = np.empty((alto_img, ancho_img))
    matriz_final = np.empty((alto_img, ancho_img))

    col_salida = alto_img
    fil_salida = ancho_img
    for x in range(alto_img):
        col_salida -= 1
        for y in range(ancho_img):
            matriz_roja_entrada[x-1][y-1] = matriz_roja_salida[y-1][col_salida]

    # print(matriz_roja_entrada)


if __name__ == '__main__':
    rotarImagen()
