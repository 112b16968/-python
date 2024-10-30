import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex

# 讀取影像

image = io.imread("sunset.png")
#調整後的圖片
image1 = ex.adjust_gamma(image, 1.5)
#調整後的圖片
sunset1 = ex.adjust_gamma(image, 0.35)


# 顯示圖片
f = plt.figure()
plt.subplot(2, 2, 1)
plt.imshow( image1 , cmap='gray')
plt.title('Picture1')


plt.subplot(2, 2,2)
#顯示直方圖
plt.hist(image1.flatten(), bins=256 , color='gray')
plt.axis('on')

plt.subplot(2, 2, 3)
plt.imshow( sunset1, cmap='gray')
plt.title('Picture2')


plt.subplot(2, 2,4)
#顯示直方圖
plt.hist(sunset1.flatten(), bins=256 , color='gray')
plt.axis('on')


plt.show()