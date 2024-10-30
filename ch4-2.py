import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex

# 讀取影像
image = io.imread("chickens.png")
chickens1 = ex.adjust_gamma(image, 0.25 )
chickens2 = ex.adjust_gamma(image, 0.15 )

# 顯示圖片
plt.subplot(1, 2, 1)
plt.imshow(chickens1 , cmap='gray')
plt.title('Picture1')
plt.axis('off')


plt.subplot(1, 2, 2)
plt.imshow(chickens2 , cmap='gray')
plt.title('Picture2')
plt.axis('off')

plt.show()