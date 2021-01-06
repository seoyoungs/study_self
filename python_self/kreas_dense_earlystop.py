##########earlystopping

import numpy as np

a = np.array(range(1,101))
size=6

def split_x(seq, size) :
    aaa=[]
    for i in range(len(seq) -size + 1):
        subset = seq [i : (i+size)]
        aaa.append(subset)
    print(type(aaa))
    return np.array(aaa)

dataset= split_x(a, size)

x= dataset[:, :5] #(95, 5)
y= dataset[:, -1] #(95,)
#print(x.shape)
#print(y.shape)

b= np.array(range(96,106))
dataset= split_x(b,6)
x_pred= dataset[:, :5]
y_pred= dataset[:, -1]
# print(x_pred.shape) #(5,5)

#####train_test_split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.8, random_state=66)
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, train_size=0.8, random_state=66)

###전처리
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
x_val = scaler.transform(x_val)
x_pred = scaler.transform(x_pred)


#2.모델 구성
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, LSTM

model=Sequential()
model.add(Dense(20, activation='relu', input_dim=5))
model.add(Dense(10))
model.add(Dense(10))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss = 'mse',optimizer = 'adam')

from tensorflow.keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=10, mode='auto')
model.fit(x_train, y_train, epochs=500, batch_size=4, validation_data=(x_val, y_val),
           callbacks=[early_stopping])

#4. 평가,예측
loss= model.evaluate(x_test, y_test, batch_size=4) 
print('loss :', loss)
y_pred=model.predict(x_pred)
print('y_pred:', y_pred)

'''
LSTM_전처리 적용 전
loss : 0.003982500173151493
<class 'list'>
[[100.90845]
 [101.94296]
 [102.92134]
 [103.93193]
 [104.92702]]

LSTM_전처리 적용
loss : 12.677891731262207
y_pred: [[104.80475 ]
 [106.178635]
 [107.507385]
 [108.888985]
 [110.16263 ]]

Dense_전처리만 적용
loss : 0.011262037791311741
<class 'list'>
[[101.05299 ]
 [102.06226 ]
 [103.06417 ]
 [104.079895]
 [105.00525 ]]

Dense_전처리, early_stopping 적용
loss : 0.00040118928882293403
y_pred: [[101.04163]
 [102.03986]
 [103.04012]
 [104.04966]
 [104.97659]]

 결과->Dense_전처리, early_stopping가 더 프로그램빨리 돌아가고 값이 더 정확하다.
'''