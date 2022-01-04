Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=10
x
10
y='Hello, world!'
y
'Hello, world!'
type(x)
<class 'int'>
type(y)
<class 'str'>
x,y,z=10,20,30
x;y;z
10
20
30
x=y=z=10
x;y;z
10
10
10
x,y=10,20
x,y=y,x
x;y
20
10
x=10
del x
x
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x
NameError: name 'x' is not defined
x=None
print(x)
None
x
# 아무것도 출력되지 않음

a=10; b=20
c = a+b
c
30
a=10
a=a+20
a
30
a += 20
a
50
x=-10
+x
-10
-x
10

input()
Hello, world!
'Hello, world!'
x = input()
Hello, world!
x
'Hello, world!'
x = input('문자열을 입력하세요: ')
문자열을 입력하세요: Hello, world!
x
'Hello, world!'

a = input('첫번째 숫자를 입력하세요: ')
첫번째 숫자를 입력하세요: 10
b = input('두번째 숫자를 입력하세요: ')
두번째 숫자를 입력하세요: 20
print(a+b)
1020
type(a)
<class 'str'>
a=int(input('첫번째 숫자를 입력하세요: '))
첫번째 숫자를 입력하세요: 10
b=int(input('두번째 숫자를 입력하세요: '))
두번째 숫자를 입력하세요: 20
print(a+b)
30
a,b=input('문자열 두 개를 입력하세요: ').split()
문자열 두 개를 입력하세요: Hello Python
print(a); print(b)
Hello
Python
a,b=input('숫자 두 개를 입력하세요: ').split()
숫자 두 개를 입력하세요: 10 20
a=int(a); b=int(b)
print(a+b)
30
map(int, input('숫자 두 개를 입력하세요: ').split())
숫자 두 개를 입력하세요: 10 20
<map object at 0x000001E69E37B5B0>
print(a+b)
30
a,b=map(int, input('숫자 두 개를 입력하세요: ').split())
숫자 두 개를 입력하세요: 10 20
print(a+b)
30
a,b=map(int, input('숫자 두 개를 입력하세요: ').split(,))
SyntaxError: invalid syntax
a,b=map(int, input('숫자 두 개를 입력하세요: ').split(','))
숫자 두 개를 입력하세요: 10,20
print(a+b)
30

# 연습문제
a,b,c=map(int, input().split())
-10 20 30
print(a+b+c)
40

# 심사문제
a = 50; b = 100; c = None
print(a); print(b); print(c)
50
100
None
kr,en,ma,sc=map(int, input().split())
32
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    kr,en,ma,sc=map(int, input().split())
ValueError: not enough values to unpack (expected 4, got 1)
kr,en,ma,sc=map(int, input().split())
32 53 22 95
print((kr+en+ma+sc)//4)
50
