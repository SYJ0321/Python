Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

import turtle as t
t.shape('turtle')
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
import turtle as t
t.shape('turtle')
for i in rane(4):
    t.forward(100)
    t.right(90)

    
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for i in rane(4):
NameError: name 'rane' is not defined. Did you mean: 'range'?
for i in range(4):
    t.forward(100)
    t.right(90)

    
# 오각형 그리기
import turtle as t
t.shape('turtle')
t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    t.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
import turtle as t
t.shape('turtle')
for i in range(5):
    t.forward(100)
    t.right(360/5)

    
# 다각형 그리기
n = int(input())
6
t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    t.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
import turtle as t
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right(360/n)

    
# 다각형에 색칠하기
import turtle as t
n = 6
t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
import turtle as t
t.shape('turtle')
t.color('red')
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right(360/n)

    
t.end_fill()

# 원 그리기
import turtle as t
t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    t.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
import turtle as t
t.shape('turtle')
t.circle(120)

# 원을 반복해서 그리기
import turtle as t
n = 60
t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    t.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.circle(120)
    t.right(360/n):
        
SyntaxError: invalid syntax
for i in range(n):
    t.circle(120)
    t.right(360/n)

    
# 선으로 복잡한 무늬 그리기
import turtle as t
t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
t.shape('turtle')
t.speed('fastest')
for i in range(300):
    t.forward(i)
    t.right(91)

    
# 연습문제
import turtle as t
n=5
t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    t.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.right(72)

    
for i in range(n):
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.left(72)

    
t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    t.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.left(72)

    
for i in range(n):
    t.forward(100)
    t.right((360/n)*2)
    t.forward(100)
    t.left(360/n)

    
# 심사문제
import turtle as t
n, line = map(int, input().split())
5 150
t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    t.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.forward(line)
    t.right((360/n)*2)
    t.forward(line)
    t.left(360/n)

    
