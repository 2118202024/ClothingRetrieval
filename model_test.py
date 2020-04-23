"""
标签	所代表的意思
0	短袖圆领T恤
1	裤子
2	套衫
0	连衣裙
4	外套
5	凉鞋
6	衬衫
7	1
8	包
9	短靴
"""
# please note, all tutorial code are running under python3.5.
# If you use the version like python2.7, please modify the code accordingly

# 6 - CNN example

# to try tensorflow, un-comment following two lines
# import os
# os.environ['KERAS_BACKEND']='tensorflow'
import keras
import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten
from keras.optimizers import Adam
from keras.models import load_model

cloth_dict={
0	:'牛仔裤',
1	:'鞋子',
2	:'双肩背包',
3   :'长袖外套',
4   :'鸭舌帽',
5   :'连衣裙'
}

model = load_model('my_model.h5')
# 训练模型
# 评估模型
import cv2
import matplotlib.pyplot as plt

for i in range(0,30):
    img=cv2.imread("picture/0/3-%s.jpg"%i)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray=cv2.resize(gray,(220,220))
    gray = gray.reshape(-1, 1,220, 220)/255.
    print("预测值  ：", cloth_dict[int(np.argmax(model.predict(gray), axis=1))])
    print("真实  ：",0)		# 打印最大概率对应的标签
    cv2.imshow("1",img)
    cv2.waitKey(0)
    # cv2.imshow("1",img)
    # cv2.waitKey(0)
