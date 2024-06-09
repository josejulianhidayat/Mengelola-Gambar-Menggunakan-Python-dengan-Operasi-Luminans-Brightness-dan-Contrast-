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
# Fungsi untuk mengubah kontras
def change_contrast(Image, alpha, beta):
    contrast_image = cv2.convertScaleAbs(Image, alpha=alpha, beta=beta)
    return contrast_image

# Mengubah kontras
contrast_image = change_contrast(Image, 1.5, 100)  # alpha > 1 meningkatkan kontras, alpha < 1 menurunkan kontras

# Menampilkan hasil
plt.imshow(cv2.cvtColor(contrast_image, cv2.COLOR_BGR2RGB))
plt.title('Kontras Diubah')
plt.show()
