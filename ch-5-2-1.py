#匯入所需的模組
import skimage.io as io 
import numpy as np
from skimage.draw import polygon 
import skimage.util as ut 
import scipy.ndimage as fl
# 讀取影像
m2 = io. imread('pelicans.png')
# 獲取影像的大小
r, c = m2. shape
# 建立ROI
xi = np.array([200, 200 ,400, 400])  # x座標
yi = np.array([310, 500 ,500, 310])  # y座標
# 創建與圖像大小相同的掩碼
roi = np. zeros_like(m2) # 初始化為全黑掩碼（值為 0）
# 使用多邊形頂點生成其內部區域的行列坐標
rr, cc = polygon (yi, xi)
# 將多邊形內部設置為 1（表示感興趣的區域）
roi[cc, rr] = 1
# 保留多邊形內部的圖像區域
mr1 = m2 * roi  # 將原始圖像與掩碼相乘，保留多邊形內部，其他區域為 0
# 保留多邊形外部的圖像區域
mr2 = m2 * (1 - roi)  # 將原始圖像與反向掩碼相乘，保留多邊形外部，其他區域為 0
# 顯示多邊形外部的區域
io.imshow(mr2)  # 顯示結果圖像（多邊形外部）
io.show()  # 顯示窗口

