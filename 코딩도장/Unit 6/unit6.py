# 변수 할당
x=10
x
# 10
y='Hello, world!'
y
# 'Hello, world!'

# 변수 자료형
type(x)
# <class 'int'>
type(y)
# <class 'str'>

# 변수 여러 개 만들기
x,y,z=10,20,30
x;y;z
# 10
# 20
# 30

x=y=z=10
x;y;z
# 10
# 10
# 10

x,y=10,20
x,y=y,x
x;y
# 20
# 10

# 변수 제거
x=10
del x
x
# Traceback (most recent call last):
#   File "<pyshell#15>", line 1, in <module>
#     x
# NameError: name 'x' is not defined

# 빈 변수 만들기
x=None
print(x)
# None
x
# 아무것도 출력되지 않음

# 변수의 연산
a=10; b=20
c = a+b
c
# 30

a=10
a=a+20
a
# 30
a += 20
a
# 50

x=-10
+x
# -10
-x
# 10

# 입력값을 변수에 저장하기
input()
# Hello, world!
# 'Hello, world!'

x = input()
# Hello, world!
x
# 'Hello, world!'

x = input('문자열을 입력하세요: ')
# 문자열을 입력하세요: Hello, world!
x
# 'Hello, world!'

a = input('첫번째 숫자를 입력하세요: ')
b = input('두번째 숫자를 입력하세요: ')
print(a+b)
# 첫번째 숫자를 입력하세요: 10
# 두번째 숫자를 입력하세요: 20
# 1020

type(a)
# <class 'str'>

a=int(input('첫번째 숫자를 입력하세요: '))
b=int(input('두번째 숫자를 입력하세요: '))
print(a+b)
# 첫번째 숫자를 입력하세요: 10
# 두번째 숫자를 입력하세요: 20
# 30

a,b=input('문자열 두 개를 입력하세요: ').split()
# 문자열 두 개를 입력하세요: Hello Python
print(a); print(b)
# Hello
# Python

# input의 결과를 정수형으로 바꾸기
a,b=map(int, input('숫자 두 개를 입력하세요: ').split())
# 숫자 두 개를 입력하세요: 10 20
print(a+b)
# 30

a,b=map(int, input('숫자 두 개를 입력하세요: ').split(','))
# 숫자 두 개를 입력하세요: 10,20
print(a+b)
# 30

# 연습문제
a,b,c=map(int, input().split())
# -10 20 30
print(a+b+c)
# 40

# 심사문제 1
a = 50; b = 100; c = None
print(a); print(b); print(c)
# 50
# 100
# None

# 심사문제 2
kr,en,ma,sc=map(int, input().split())
print((kr+en+ma+sc)//4)
# 32 53 22 95
# 50
