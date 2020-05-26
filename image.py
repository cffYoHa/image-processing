from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

# 画像の読み込み & グレースケールに変換
img = Image.open('sample1.pgm').convert('L')

# 上段の画像の表示設定
plt.subplot(2, 1, 1) # 引数はそれぞれ、全体の行数、全体の列数、設定対象のIndex
a = np.array(img)
plt.imshow(a)
plt.gray()
plt.axis('off')

# 下段のヒストグラムの設定
plt.subplot(2, 1, 2)
plt.hist(a.flatten(), bins=np.arange(256 + 1)) #階級の幅を1としてヒストグラムを出す。

# 図表の表示
plt.show()