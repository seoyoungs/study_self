from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# seed 값 설정
seed =0
np.random.seed(seed)
tf.random.set_seed(3)

# 데이터 입력
df_pre = pd.read_csv('C:/data/deeplearning/dataset/wine.csv', index_col=0, header=0)
# df = df_pre.sample(frac=1)
# dataset = df_pre.Values
x = df_pre.iloc[:, 0:12]
y = df_pre.iloc[:, -1]
# y --> 0,1 로 구성 (binary)
x= x.to_numpy()
y= y.to_numpy()

# 모델 설정
model = Sequential()
model.add(Dense(30, input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile
model.compile(loss = 'binary_crossentropy',
               optimizer='adam', metrics=['acc'])

# fit
model.fit(x,y, batch_size=8, epochs=100)

# print
print('\n Accuracy: %.4f' % (model.evaluate(x,y)[1]))

# 저장 폴더 만들기
import os
Model_Dir = '../data/h5/'
if not os.path.exists(Model_Dir):
    os.mkdir(Model_Dir)

modelpath = '../data/h4/{epochs:02d}-{val_loss:.4f}.hdf5'

cp = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)
# save_best_only 저장한 모델이 나아졌을 때만 저장하게끔 할때 쓴다

model.fit(x,y, validation_split=0.2, epochs=100, callbacks=[cp])
