import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar
image = cv2.imread('Image.jpg')

# Menampilkan gambar asli
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Gambar Asli')
plt.show()