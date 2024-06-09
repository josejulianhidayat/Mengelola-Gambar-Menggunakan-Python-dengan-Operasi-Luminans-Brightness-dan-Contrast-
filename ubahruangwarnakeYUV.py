import cv2
import numpy as np
from matplotlib import pyplot as plt

import cv2

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


# Mengubah ke ruang warna YUV
yuv_image = cv2.cvtColor(Image, cv2.COLOR_BGR2YUV)

# Modifikasi channel Y (luminans)
yuv_image[:,:,0] = cv2.equalizeHist(yuv_image[:,:,0])

# Mengubah kembali ke BGR
luminance_adjusted = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

# Menampilkan hasil
plt.imshow(cv2.cvtColor(luminance_adjusted, cv2.COLOR_BGR2RGB))
plt.title('Luminans Diubah')
plt.show()
