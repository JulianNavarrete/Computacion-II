from PIL import Image


def rotarImagen():
    # ubic = str(input("Ingrese el nombre de la imagen con su respectiva extensión: "))
    ubic = "yacht.ppm"
    im = Image.open(ubic)
    im_copia = im

    matriz_roja = []
    matriz_verde = []
    matriz_azul = []

    for i in range(im_copia.size[0]):
        matriz_roja.append([0] * im_copia.size[1])
        matriz_verde.append([0] * im_copia.size[1])
        matriz_azul.append([0] * im_copia.size[1])

    for i in range(im_copia.size[0]):
        for j in range(im_copia.size[1]):
            r, g, b = im_copia.getpixel((i, j))
            matriz_roja[i][j] = r
            matriz_verde[i][j] = g
            matriz_azul[i][j] = b


if __name__ == '__main__':
    rotarImagen()

