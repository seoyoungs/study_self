# 9강
'''
고급경사 하강법
1. 확률적 경사 하강법(SGD)
2 .모덴텀(Momentum)
3. 네스테로프 모멘텀(NAG)
4. 아다그라드(Adagrad)
5. 알엠에스프롭 (RMSProp)
6. 아담(Adam)
'''

# 10장 모델 설계하기
# 폐암수술 환자 생존율

#딥러닝 구동하는 케라스 함수 호출
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#필요한 라이브러이 호출
import numpy as np
import tensorflow as tf

# 실행 할 때마다 같은 결과 나오기 위해 생성하는 부분
np.random.seed(3)
tf.random.set_seed(3) #global random seed를 설정해주는 함수(미리 설정시 동일한 결과 도출가능)

#준비된 수술 환자 데이터를 불러옴
data_set = np.loadtst('C:/data/every_deeplearning/dataset/ThoraricSurgery.csv', delimiter=",")

# 환자의 기록과 수술 결과를 x,y로 구분하여 저장
x= data_set[:, 0:17]
y= data_set[:, 17]

#딥러닝 구조 설정, 실행
model = Sequential()
model.add(Dense(30, input_dim=17, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 훈련
model.compile(loss = 'mse', optimizer='adam', metrics=['acc'])
model.fit(x,y, epochs=100, batch_size=10)






