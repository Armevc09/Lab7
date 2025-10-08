#Ej1P2 Crea una carpeta llamada "colores" con 3 imágenes de 3 colores diferentes.
#Luego, con OpenCV, abre cada imagen e imprime el valor del color en la terminal.

import cv2
import numpy as np
import os

if not os.path.exists("colores"):
    os.makedirs("colores")

red_image = np.zeros((100, 100, 3), dtype=np.uint8)
green_image = np.zeros((100, 100, 3), dtype=np.uint8)
blue_image = np.zeros((100, 100, 3), dtype=np.uint8)

red_image[:, :] = [0, 0, 255]
green_image[:, :] = [0, 255, 0]
blue_image[:, :] = [255, 0, 0]

cv2.imwrite("colores/red.jpg", red_image)
cv2.imwrite("colores/green.jpg", green_image)
cv2.imwrite("colores/blue.jpg", blue_image)

for color in ["red", "green", "blue"]:
    img = cv2.imread(f"colores/{color}.jpg")
    print(f"{color} image:")
    print("Color values (BGR):", img[0, 0]) 
    print()
    cv2.imshow(f"{color} image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#2. A partir del ejercicio anterior, crea una función que convierta 
#el color RGB a escala de grises.

def rgb_to_grayscale(r, g, b):
    gray = 0.299 * r + 0.587 * g + 0.114 * b
    return int(gray)


r, g, b = 255, 0, 0 
gray_value = rgb_to_grayscale(r, g, b)
print("Grayscale value of RGB(255, 0, 0):", gray_value)

#3. Clase para procesar imágenes
import cv2

class ImageProcessor:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
    
    def convert_to_rgb(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
    
    def convert_to_hsv(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
    
    def convert_to_grayscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    
    def show_image(self, image, title="Image"):
        cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Ejemplo de uso
image_processor = ImageProcessor("colores/red.jpg")
rgb_image = image_processor.convert_to_rgb()
hsv_image = image_processor.convert_to_hsv()
gray_image = image_processor.convert_to_grayscale()

# Mostrar imágenes
image_processor.show_image(rgb_image, "RGB Image")
image_processor.show_image(hsv_image, "HSV Image")
image_processor.show_image(gray_image, "Grayscale Image")

#4 . con hsv detectamos rojo verde y azul
import cv2
import numpy as np

def detect_color_hsv(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    lower_green = np.array([50, 100, 100])
    upper_green = np.array([70, 255, 255])
    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])

    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)

    if cv2.countNonZero(mask_red) > 0:
        return "Red"
    elif cv2.countNonZero(mask_green) > 0:
        return "Green"
    elif cv2.countNonZero(mask_blue) > 0:
        return "Blue"
    else:
        return "Color not detected"
    
color = detect_color_hsv("colores/green.jpg")
print("Detected color:", color)

#5. con la camara wb mostramos fotograma en escala de grises y rgb
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow('Grayscale Frame', gray_frame)
    cv2.imshow('RGB Frame', rgb_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

#6 captura fotograma gardamos y alicamos filtro ene scala de grises y lueg
#dividimos en cuadrantes

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("Webcam", frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('c'):  # Capturar la imagen y guardarla
        cv2.imwrite("Captures/image1.jpg", frame)
        print("Image saved as Captures/image1.jpg")
    
    if key == ord('q'):  # Salir con la tecla 'q'
        break

cap.release()
cv2.destroyAllWindows()

# Aplica el filtro de escala de grises a la imagen capturada
image = cv2.imread("Captures/image1.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("Captures/gray_image.jpg", gray_image)

# Dividir la imagen en cuadrantes
height, width = image.shape[:2]
half_height, half_width = height // 2, width // 2

quadrant1 = image[:half_height, :half_width]
quadrant2 = image[:half_height, half_width:]
quadrant3 = image[half_height:, :half_width]
quadrant4 = image[half_height:, half_width:]

# Mostrar los cuadrantes
cv2.imshow("Quadrant 1", quadrant1)
cv2.imshow("Quadrant 2", quadrant2)
cv2.imshow("Quadrant 3", quadrant3)
cv2.imshow("Quadrant 4", quadrant4)
cv2.waitKey(0)
cv2.destroyAllWindows()

