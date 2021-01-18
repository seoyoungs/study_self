#모두의 파이썬 ch3

# #몇분 몇초인지 계산
sec= 1000
min = 1000//60  ##나눗셈 코딩//
remainder = 1000 % 60 ###1000/60 한 나눗셈의 나머지
print(min, remainder) ##16 40 --> 1000초는 16분 40초이다.

"""
#매출 관련 코딩
americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500

americanos = int(input('아메리카노 판매개수 : ')) ##int 정수형으로 변환
cafelattes = int(input('카페라테 판매개수 : '))
capucinos = int(input('카푸치노 판매 개수 : '))

sales = americanos*americano_price
sales = sales + cafelatte_price*cafelattes
sales = sales + capucinos*capucino_price
print('총 매출은', sales, '입니다.')\

#---------------------------#
결과
아메리카노 판매개수 : 10
카페라테 판매개수 : 20
카푸치노 판매 개수 : 30
총 매출은 185000 입니다.


## 몸무게와 키
weight = float(input('몸무게를 kg단위로 입력하시오 :'))
hight = float(input('키를 미터단위로 입력하시오 :'))

tmi = (weight/hight**2) # **은 제곱을 표현하는것이다.
print('당신의 BMI:', tmi)

#결과-----------------------========
몸무게를 kg단위로 입력하시오 :56
키를 미터단위로 입력하시오 :158.5
당신의 BMI: 0.0022290997024549952



"""
#연산자 팁
x= 4
y= 4
x = x + 2
print('x = x + 2의 답:',x) #x = x + 2의 답: 6
y += 2
print('y += 2의 답:',y) #y += 2의 답: 6

#결론=============
#둘은 x = x + 2, y += 2 같은 식이다.

#원기둥 부피 구하는 공식
r= 10
h= 100
vol = 3.14*r**2*h
print('원기둥의 부피:', vol) #원기둥의 부피: 31400.0

