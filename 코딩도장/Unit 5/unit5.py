# 사칙연산
1+1
# 2
1-2
# -1
2*2
# 4
5/2
# 2.5
4/2
# 2.0

#버림 나눗셈
5//2
# 2
4//2
# 2
5.5//2
# 2.0

# 기타 연산
5%2
# 1
2**10
# 1024

# 정수형으로 변환
int(3.3)
# 3
int(5/2)
# 2
int('10')
# 10

type(10)
<class 'int'>

# 몫과 나머지를 함께 구하기
divmod(5,2)
# (2, 1)
quotient, remainder = divmod(5,2)
print(quotient, remainder)
# 2 1

#2진수, 8진수, 16진수
0b110
6
0o10
8
0xF
15

#실수형으로 변환
float(5)
5.0
float(1+2)
3.0
float('5.3')
5.3

type(3.5)
<class 'float'>

# 복소수
1.2+1.3j
(1.2+1.3j)

complex(1.2,1.3)
(1.2+1.3j)

#괄호 
35+1*2
37
(35+1)*2
72

# 연습문제
print(int(0.247*12+4.159))
7
