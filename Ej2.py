# 2. Genere un programa que solicite al usuario seleccionar entre tamaño 
#original, pequeño, mediano o grande, y que redimensione la imagen.
import cv2

imagen = cv2.imread('rob.png')

if imagen is None:
    print("No se pudo cargar la imagen. Verifique la ruta.")
    exit()

tamaño = input("Seleccione el tamaño (1. original, 2. pequeño, 3. mediano, 4. grande): ")

if tamaño == "1":
    imagen_redimensionada = imagen
elif tamaño == "2":
    imagen_redimensionada = cv2.resize(imagen, (500, 500))
elif tamaño == "3":
    imagen_redimensionada = cv2.resize(imagen, (750, 750))
elif tamaño == "4":
    imagen_redimensionada = cv2.resize(imagen, (1000, 1000))
else:
    print("Tamaño no válido.")
    exit()

cv2.imwrite('imagen_redimensionada.jpg', imagen_redimensionada)

cv2.imshow('Imagen Redimensionada', imagen_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
