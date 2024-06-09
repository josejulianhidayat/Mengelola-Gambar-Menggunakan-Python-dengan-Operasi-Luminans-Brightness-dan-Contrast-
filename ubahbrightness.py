import cv2
import numpy as np
from matplotlib import pyplot as plt

# Baca gambar dari file
Image = cv2.imread('Image.jpg')

# Pastikan gambar berhasil dibaca
if Image is None:
    print("Error: Gambar tidak ditemukan atau tidak bisa dibuka.")
else:
    # Ubah ruang warna dari BGR ke YUV
    yuv_image = cv2.cvtColor(Image, cv2.COLOR_BGR2YUV)

    # Simpan gambar hasil konversi
    cv2.imwrite('path_to_save_yuv_image.jpg', yuv_image)
    print("Gambar berhasil dikonversi dan disimpan.")

# Fungsi untuk mengubah kecerahan
def change_brightness(Image, value):
    hsv = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v = np.clip(v, 0, 255)
    final_hsv = cv2.merge((h, s, v))
    bright_image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return bright_image

# Mengubah kecerahan
bright_image = change_brightness(Image, 200)

# Menampilkan hasil
plt.imshow(cv2.cvtColor(bright_image, cv2.COLOR_BGR2RGB))
plt.title('Kecerahan Diubah')
plt.show()
