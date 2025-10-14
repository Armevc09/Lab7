# 3. Cree un programa que gire 90 grados la imagen cada vez que el usuario 
# presione cualquier tecla. ¿Cuál es la diferencia entre imprimir una imagen 
# y usar imshow?
import cv2
imagen = cv2.imread('rob.png')

while True:
    cv2.imshow('Imagen', imagen)
    key = cv2.waitKey(0)
    if key == 27:
        break
    imagen = cv2.rotate(imagen, cv2.ROTATE_90_CLOCKWISE)

cv2.destroyAllWindows()