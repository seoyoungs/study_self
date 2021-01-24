#### 코딩으로 확인하는 평균 제곱 오차
import numpy as np

# 기울기 a와 y절편b
fake_a_b = [3, 76]

# x,y 의 데이터값
data = [[2, 81], [4,93], [6,91], [8,97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

# y =ax+b에 a,b 값을 대입하여 출력하는 함수
def predict(x):
    return fake_a_b[0]*x + fake_a_b[1]

#mse 힘수
def mse(y, y_hat):
    return (((y - y_hat)**2).mean())

#mse함수를 각각 y값에 대입해 최종값을 구하는 함수
def mse_val(y, predict_result):
    return mse(np.array(y), np.array(predict_result))

#예측 값이 들어갈 빈 리스트
predict_result= []

#모든 x 값을 한 번씩 대립해 
'''
for i in range(len(x)):
    #predict_result 리스트를 완성
    predict_result.append(predict(x[i]))
    print("공부한 시간 = &.f, 실제 점수 = %.f, 예측 점수 = %.f" % (x[i], y[i], predict(x[i])))
'''
for i in range(len(x)):
    # predict_result 리스트를 완성
    predict_result.append(predict(x[i]))
    print("공부한 시간 = %.f, 실제 점수 = %.f, 예측 점수 = %.f" % (x[i], y[i], predict(x[i])))


#최종 MSE 출력
print("mse 최종값: " + str(mse_val(predict_result, y)))


