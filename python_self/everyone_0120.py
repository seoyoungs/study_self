##모두의 파이썬 4장

# 문자열 안에 또 문자열 강조하기
# 철수가 '안녕'이라고 말헸습니다. --> 이문장  출력
msg = "철수가 '안녕'이라고 말했습니다."
print(msg) #철수가 '안녕'이라고 말했습니다.

# 문자열, 실수로 반환하기
#int()는 문자열을 정수로 반환, float() 문자열을 실수로 반환
'''
t1= input('정수를 반환하시오:') 
x= int(t1)
t2= input('실수를 반환하시오:') #이거는 실수라 소수점도 가능, 자연수도 가능
y= int(t2)
'''
#문자열에 변수의 삽입 값 출력= %s
price = 200
print('상품의 가격은 %s원 입니다.' %price) # price바뀌어도 적용가능

# 줄 바꿈 \n
print('말 한마디로 \n천냥 빛을 갚는다.')
#특수 문자사용 시 (/)의 역할
x= 'don\'t'
print(x) # don't (')표시 앞에 \ 해주기

##str사용하기
import time

now = time.time()
thisyear = int(1970 + now//(365*24*3600))
print("올해는"+str(thisyear)+'입니다')
age= int(input('몇살이신지요?'))
print('2050년에는' + str(age+(2050-thisyear))+'살 이신군요.')

##공백리스트 생성 []
list = []
list.append(1)
list.append(2)
list.append(5)

print(list) #[1, 2, 5]


