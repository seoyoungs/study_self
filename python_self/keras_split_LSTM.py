##########earlystopping, 전처리한것

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

x_train=x_train.reshape(-1,5,1)
x_test=x_test.reshape(-1,5,1)
x_val=x_val.reshape(-1,5,1)
x_pred = x_pred.reshape(-1,5,1)


#2.모델 구성
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, LSTM

model=Sequential()
model.add(LSTM(20, activation='relu', input_shape=(5,1)))
model.add(Dense(10))
model.add(Dense(10))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss = 'mse',optimizer = 'adam')
model.fit(x_train, y_train, validation_data=(x_val, y_val), 
          epochs=100, batch_size=4)

#4. 평가,예측
loss= model.evaluate(x_test, y_test, batch_size=4) 
print('loss :', loss)
y_pred=model.predict(x_pred)
print('y_pred:', y_pred)








