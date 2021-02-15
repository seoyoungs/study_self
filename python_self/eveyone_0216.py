from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd
import tensorflow as tf

# seed 값 설정
seed =0
np.random.seed(seed)
tf.random.set_seed(3)

df = pd.read_csv('C:/data/every_deeplearning/dataset/housing.csv', delim_whitespace=True, header=None)
dataset = df.values
x = dataset[:, 0:13]
y = dataset[:,13]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

model = Sequential()
model.add(Dense(30, input_dim=13, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1))

# 3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=200, batch_size=10)

# 4. 예측, 결과
#예측값과 실제값 비교
y_prediction = model.predict(x_test).flatten() # 여기도 1차원으로 바꿔주는 함수 .flatten() 쓸수 있다
for i in range(10):
    label = y_test[i]
    prediction = y_prediction[i]
    print("실제가격: {:.3f}, 예상가격: {:.3f}".format(label, prediction))

