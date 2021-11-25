from PIL import Image
import numpy as np


def rotarImagen():
    # ubic = str(input("Ingrese el nombre de la imagen con su respectiva extensión: "))
    ubic = "yacht.ppm"
    im = Image.open(ubic)
    alto_img = im.size[0]
    ancho_img = im.size[1]
    matriz_principal = np.asarray(im)
    # print(matriz_principal)

    matriz_roja_entrada = np.ones((alto_img, ancho_img))
    matriz_verde_entrada = np.empty((alto_img, ancho_img))
    matriz_azul_entrada = np.empty((alto_img, ancho_img))
    matriz_roja_salida = np.empty((ancho_img, alto_img))
    matriz_verde_salida = np.empty((ancho_img, alto_img))
    matriz_azul_salida = np.empty((ancho_img, alto_img))
    matriz_final = np.empty((ancho_img, alto_img))

    for x in range(alto_img):
        for y in range(ancho_img):
            r, g, b = im.getpixel((x, y))
            matriz_roja_entrada[x, y] = r
            matriz_verde_entrada[x, y] = g
            matriz_azul_entrada[x, y] = b

    col_salida = alto_img
    for x in range(alto_img):
        col_salida -= 1
        for y in range(ancho_img):
            matriz_roja_salida[y, col_salida] = matriz_roja_entrada[x, y]

    col_salida = alto_img
    for x in range(alto_img):
        col_salida -= 1
        for y in range(ancho_img):
            matriz_verde_salida[y, col_salida] = matriz_verde_entrada[x, y]

    col_salida = alto_img
    for x in range(alto_img):
        col_salida -= 1
        for y in range(ancho_img):
            matriz_azul_salida[y, col_salida] = matriz_azul_entrada[x, y]

    for x in range(alto_img):
        for y in range(ancho_img):
            matriz_final[x, y][] = (matriz_roja_salida[x, y][0], matriz_verde_salida[x, y][1], matriz_azul_salida[x, y][2])

    img_final = Image.fromarray(np.uint8(matriz_final))
    Image.Image.show(img_final)


    # print(im)
    # print(matriz_roja_entrada)
    # print(matriz_azul_salida)


if __name__ == '__main__':
    rotarImagen()
