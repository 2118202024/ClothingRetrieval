import cv2
import os

import numpy as np
def load_data():
    bath="./picture/"
    list1=os.listdir(bath)
    Alldata=[]
    Alllabel=[]
    for i in list1[:5]:
        cloth_list=os.listdir(bath+i)
        for cloth_path in cloth_list:
            pa=bath+i+"/"+cloth_path
            data=cv2.imread(pa,cv2.IMREAD_GRAYSCALE)
            Alldata.append(data)
            Alllabel.append(int(i))

    Alldata = np.array(Alldata)
    Alllabel = np.array(Alllabel)
    print(Alldata.shape)
    r = np.random.permutation(Alldata.shape[0])
    new_train_X = Alldata[r, :, :]
    new_train_Y = Alllabel[r]
    # new_train_X = Alldata
    # new_train_Y = Alllabel
    t=int(len(new_train_Y)/10*9)
    x_train=new_train_X[0:t]
    x_test=new_train_X[t:]
    y_train=new_train_Y[0:t]
    y_test=new_train_Y[t:]
    return (x_train, y_train), (x_test, y_test)
if __name__ == '__main__':
    (x_train, y_train), (x_test, y_test)=load_data()
    print(x_train.shape)
    print(y_train.shape)
