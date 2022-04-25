import requests
import img2pdf
import os

"""
    https://parzibyte.me/blog
"""


def descargar_imagen(url_base, nombre):
    url_imagen = f"{url_base}{nombre}.jpg"
    print(f"Descargando {url_imagen}...")
    nombre_local_imagen = f"{nombre}.jpg"
    imagen = requests.get(url_imagen).content
    print("Guardando...", end="")
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
    print("OK")
    return nombre_local_imagen


def descargar_libro(url_base, paginas):
    inicio = 0
    imagenes = []
    # Descargar imágenes y agregar la ruta de la imagen descargada al arreglo
    for i in range(inicio, paginas+1):
        numero_con_ceros_a_la_izquierda = f"{i:03d}"
        nombre_imagen_descargada = descargar_imagen(
            url_base, numero_con_ceros_a_la_izquierda)
        imagenes.append(nombre_imagen_descargada)
    # Convertir las imágenes a PDF y obtener el archivo como un montón de bytes
    bytes = img2pdf.convert(imagenes)
    # Eliminar las imágenes, pues ya no las necesitamos
    for imagen in imagenes:
        os.remove(imagen)
    return bytes
