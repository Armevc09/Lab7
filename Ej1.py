# 1. Cree un programa que abra una imagen y la redimensionamos a 1000x1000 pixeles
#usando open cv
import cv2
imagen = cv2.imread('rob.png')
imagen_redimensionada = cv2.resize(imagen, (1000, 1000))
cv2.imwrite('imagen_redimensionada.jpg', imagen_redimensionada)

