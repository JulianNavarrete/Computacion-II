from PIL import Image
import numpy as np


def rotarImagen(ubic):
    im = Image.open(ubic)
    # im.show()
    alto_img = im.size[0]
    ancho_img = im.size[1]
    im_copia = im
    matriz_principal = np.asarray(im)

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

    lista = []
    for x in range(ancho_img):
        for y in range(alto_img):
            pixel = tuple([int(matriz_roja_salida[x, y]), int(matriz_verde_salida[x, y]), int(matriz_azul_salida[x, y])])
            # print(pixel)
            # matriz_final[x, y] = pixel

    img_final = Image.fromarray(np.uint8(ar))
    Image.Image.show(img_final)

    '''for x in range(ancho_img):
        for y in range(alto_img):
            pixel = tuple([int(matriz_roja_salida[x, y]), int(matriz_verde_salida[x, y]), int(matriz_azul_salida[x, y])])
            im_copia.putpixel((x, y), pixel)
            # print(x,y)
    Image.Image.show(im_copia)'''


if __name__ == '__main__':
    # ubic = input("Ingrese el nombre de la imagen con su respectiva extensión: ")
    ubic = "yacht.ppm"
    rotarImagen(ubic)
