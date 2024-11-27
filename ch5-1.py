#匯入所需的模組
import skimage.io as io
from numpy import array
from numpy import float32
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
# 讀取影像
c = io.imread("cameraman.png")
#濾波器
f = array([[1,-2,1] , [-2,4,-2] , [1,-2,1]])
#濾波操作
cf2 = ndi.convolve(float32(c) , f , mode="constant")
#獲取最大最小值
maxcf2 = cf2.max()
mincf2 = cf2.min()
#將數值範圍縮到[0,1]
cf2c = (cf2 - mincf2) / (maxcf2 - mincf2)
#縣示圖
a = plt.figure()
plt.subplot(1, 2, 1)
#顯示濾波後的影像
plt.imshow( cf2c , cmap='gray')
plt.title('Picture1')
plt.axis('off')

plt.subplot(1,2 ,2)
#將濾波結果除以 60 並顯示為灰度圖
plt.imshow(cf2 / 60 , vmax = 1.0 , vmin = 0.0 , cmap = "gray")
plt.title('Picture2')
plt.axis('off')
plt.show()
