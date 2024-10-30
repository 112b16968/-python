# 匯入所需的模組
from skimage import io
import matplotlib.pyplot as plt
from numpy import float64
from numpy import uint8
import numpy as np

# 讀取影像
b1 = io.imread("blocks.jpg")

# 轉換為灰階影像
b = float64(b1)
b2 = uint8(np.clip((b//64)*64, 0, 255)) # (b//64)*64

# 顯示原始影像和低解析度影像
plt.subplot(1, 2, 1)
plt.imshow(b1 ,cmap='gray')
plt.title('Before')
plt.axis('off')


plt.subplot(1, 2, 2)
plt.imshow(b2 ,cmap='gray')
plt.title('After')
plt.axis('off')

plt.show()


