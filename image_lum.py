import cv2  #OpenCVのインポート
import matplotlib.pyplot as plt #matplotlib.pyplotのインポート

fname = "test.png" #画像ファイル名
img = cv2.imread(fname) #画像を読み出しオブジェクトimgに代入

hist_b = cv2.calcHist([img],[0],None,[256],[0,256]) #B(青)のヒストグラムを計算
plt.plot(hist_b,color = "b") #B(青)のヒストグラムをプロット

hist_g = cv2.calcHist([img],[1],None,[256],[0,256]) #G(緑)のヒストグラムを計算
plt.plot(hist_g,color = "g") #G(緑)のヒストグラムをプロット

hist_r = cv2.calcHist([img],[2],None,[256],[0,256]) #R(赤)のヒストグラムを計算
plt.plot(hist_r,color = "r") #R(赤)のヒストグラムをプロット

plt.show() #プロットを表示