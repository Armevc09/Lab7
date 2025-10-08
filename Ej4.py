#4. Con OpenCV, lea una imagen y realice las siguientes operaciones: 
#• Lea la imagen y muéstrela. 
#• Redimensione la imagen a 400x600 (ancho, alto). 
#• Corte la imagen horizontalmente y muestre las dos mitades. 
#• Corte la imagen verticalmente y muestre las dos mitades. 
#• Divida la imagen en cuadrantes del mismo tamaño y muéstrelos
#  con el título "Cuadrante N" según el número de cuadrantes. import cv2 import matplotlib.pyplot as plt

import cv2
import matplotlib.pyplot as plt

# 1. Leer la imagen
image = cv2.imread('rob.png')  # Asegúrate de que el nombre y la ruta sean correctos

if image is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta.")
    exit()  # Detiene el programa si no se puede cargar la imagen

# Convertir de BGR (formato de OpenCV) a RGB (para mostrar correctamente con matplotlib)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 2. Mostrar la imagen original
plt.imshow(image_rgb)
plt.title('Imagen Original')
plt.axis('off')
plt.show()

# 3. Redimensionar la imagen a 400x600 (ancho, alto)
resized_image = cv2.resize(image, (600, 400))

# Convertir a RGB para mostrar correctamente
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

# Mostrar la imagen redimensionada
plt.imshow(resized_image_rgb)
plt.title('Imagen Redimensionada (400x600)')
plt.axis('off')
plt.show()

# 4. Corte horizontal de la imagen
height, width, _ = image.shape
top_half = image[:height//2, :]
bottom_half = image[height//2:, :]

# Mostrar las dos mitades horizontales
top_half_rgb = cv2.cvtColor(top_half, cv2.COLOR_BGR2RGB)
bottom_half_rgb = cv2.cvtColor(bottom_half, cv2.COLOR_BGR2RGB)

plt.subplot(1, 2, 1)
plt.imshow(top_half_rgb)
plt.title('Mitad Superior')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(bottom_half_rgb)
plt.title('Mitad Inferior')
plt.axis('off')

plt.show()

# 5. Corte vertical de la imagen
left_half = image[:, :width//2]
right_half = image[:, width//2:]

# Mostrar las dos mitades verticales
left_half_rgb = cv2.cvtColor(left_half, cv2.COLOR_BGR2RGB)
right_half_rgb = cv2.cvtColor(right_half, cv2.COLOR_BGR2RGB)

plt.subplot(1, 2, 1)
plt.imshow(left_half_rgb)
plt.title('Mitad Izquierda')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(right_half_rgb)
plt.title('Mitad Derecha')
plt.axis('off')

plt.show()

# 6. Dividir la imagen en cuadrantes
quadrant_1 = image[:height//2, :width//2]
quadrant_2 = image[:height//2, width//2:]
quadrant_3 = image[height//2:, :width//2]
quadrant_4 = image[height//2:, width//2:]

# Mostrar los cuadrantes
quadrants = [quadrant_1, quadrant_2, quadrant_3, quadrant_4]
titles = ['Cuadrante 1', 'Cuadrante 2', 'Cuadrante 3', 'Cuadrante 4']

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(cv2.cvtColor(quadrants[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.show()
