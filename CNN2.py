

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
import MyLoadData
# download the mnist to the path '~/.keras/datasets/' if it is the first time to be called
# training x shape (60000, 28x28), Y shape (60000, ). test x shape (10000, 28x28), Y shape (10000, )
(x_train, y_train), (x_test, y_test) = MyLoadData.load_data()

# data pre-processing
x_train = x_train.reshape(-1, 1,220, 220)/255.
x_test = x_test.reshape(-1, 1,220, 220)/255.
y_train = np_utils.to_categorical(y_train, num_classes=5)
y_test = np_utils.to_categorical(y_test, num_classes=5)

# Another way to build your CNN

model = Sequential()
model.add(Convolution2D(
    batch_input_shape=(None, 1, 220, 220),
    filters=32,
    kernel_size=7,
    strides=1,
    padding='same',     # Padding method
    data_format='channels_first',
))
model.add(Conv2D(64, activation='relu',
                 nb_row=5,
                 nb_col=5))
model.add(Conv2D(64, activation='relu',
                 nb_row=3,
                 nb_col=3))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.35))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation='softmax'))
model.compile(loss=keras.metrics.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
model.summary()

print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)
print(x_train.shape[0], 'xtrain samples')
print(y_train.shape[0], 'ytrain samples')
print(x_test.shape[0], 'xtest samples')
print(y_test.shape[0], 'ytest samples')


model.fit(x_train, y_train, batch_size=128, epochs=20,
          verbose=1, validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])

model.save('my_model.h5')