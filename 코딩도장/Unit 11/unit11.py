Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [0,10,20,30,40,50,60,70,80,90]
30 in a
True
100 in a
False
100 not in a
True
43 in (38,76,43,62,19)
True
1 in range(10)
True
'P' in 'Hello, Python'
True
a = [10.20.30]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a = [10,20,30]; b = [9,8,7,6]
a+b
[10, 20, 30, 9, 8, 7, 6]
range(0,10) + range(10,20)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    range(0,10) + range(10,20)
TypeError: unsupported operand type(s) for +: 'range' and 'range'
list(range(0,10)) + list(range(10,20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
'Hello, '+'world!'
'Hello, world!'
'Hello, ' + 10
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    'Hello, ' + 10
TypeError: can only concatenate str (not "int") to str
'Hello, ' + str(10)
'Hello, 10'

[0,10,20,30]*3
[0, 10, 20, 30, 0, 10, 20, 30, 0, 10, 20, 30]
range(0,5,2) * 3
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    range(0,5,2) * 3
TypeError: unsupported operand type(s) for *: 'range' and 'int'
tuple(range(0,5,2)) * 3
(0, 2, 4, 0, 2, 4, 0, 2, 4)
'Hello, ' * 3
'Hello, Hello, Hello, '

a = [0,10,20,30,40,50,60,70,80,90]
len(a)
10
b = (38,76,43,62,19)
len(b)
5
len(range(0,10,2))
5
hello = 'Hello, world!'
len(hello)
13
hello = '안녕하세요'
len(hello.encode('utf-8'))
15
a = [38, 21, 53, 62, 19]
a[0]
38
a[2]
53
b = (38,21,53,62,19)
b[0]
38
r=range(0,10,2)
r[2]
4
hello = 'Hello, world!'
hello[7]
'w'
a = [38,21,53,62,19]
a._getitem_(1)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a._getitem_(1)
AttributeError: 'list' object has no attribute '_getitem_'. Did you mean: '__getitem__'?
a.__getitem__(1)
21
a[-1]
19
a[5]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a[5]
IndexError: list index out of range
# 마지막 요소에 접근
a[len(a)-1]
19

# 요소에 값 할당
a = [0,0,0,0,0]
a[0] = 38
a[1] = 21
a[2] = 53
a[3] = 62
a[4] = 19
a
[38, 21, 53, 62, 19]
a[5] = 90
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a[5] = 90
IndexError: list assignment index out of range
b = (0,0,0,0,0)
b[0] = 38
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b[0] = 38
TypeError: 'tuple' object does not support item assignment
r = range(0,10,2)
r[0]=3
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    r[0]=3
TypeError: 'range' object does not support item assignment
hello = 'Hello, world!'
hello[0]
'H'
hello[0] = 'A'
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    hello[0] = 'A'
TypeError: 'str' object does not support item assignment
a = [38,21,53,62,19]
del a[2]
a
[38, 21, 62, 19]
b = (38,21,53,62,19)
del b[2]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    del b[2]
TypeError: 'tuple' object doesn't support item deletion
r = range(0,10,2)
del r[2]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    del r[2]
TypeError: 'range' object doesn't support item deletion
hello = 'Hello, world!'
del hello[2]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    del hello[2]
TypeError: 'str' object doesn't support item deletion

# 슬라이스
a = [0,10,20,30,40,50,60,70,80,90]
a[0:4]
[0, 10, 20, 30]
a[1:1]
[]
a[1:2]
[10]
a[4:-1]
[40, 50, 60, 70, 80]

a[2:8:3]
[20, 50]

# 인덱스 생략
a[:7]
[0, 10, 20, 30, 40, 50, 60]
a[7:]
[70, 80, 90]
a[:]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[:7:2]
[0, 20, 40, 60]
a[7::2]
[70, 90]
a[::2]
[0, 20, 40, 60, 80]
a[::]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[5:1:-1]
[50, 40, 30, 20]
a[::-1]
[90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
a[0:len(a)]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

b = (0,10,20,30,40,50,60,70,80,90)
b[4:7]
(40, 50, 60)
b[4:]
(40, 50, 60, 70, 80, 90)
b[:7:2]
(0, 20, 40, 60)

r = range(10)
r
range(0, 10)
r[4:7]
range(4, 7)
r[4:]
range(4, 10)
r[:7:2]
range(0, 7, 2)

hello = 'Hello, world!'
hello[2:9]
'llo, wo'
hello[:9:2]
'Hlo o'

# 슬라이스 객체
s = slice(4,7)
range(10)[s]
range(4, 7)
range(10).__getitem__(s)
range(4, 7)
a[s]
[40, 50, 60]
hello[s]
'o, '

# 슬라이스에 요소 할당
a[2:5] = ['a','b','c']
a
[0, 10, 'a', 'b', 'c', 50, 60, 70, 80, 90]
a = [0,10,20,30,40,50,60,70,80,90]
a[2:5] = ['a]
          
SyntaxError: unterminated string literal (detected at line 1)
a[2:5] = ['a']
          
a
          
[0, 10, 'a', 50, 60, 70, 80, 90]
a = [0,10,20,30,40,50,60,70,80,90]
          
a[2:5] = ['a','b','c','d','e']
          
a
          
[0, 10, 'a', 'b', 'c', 'd', 'e', 50, 60, 70, 80, 90]
a = [0,10,20,30,40,50,60,70,80,90]
          
a[2:8:2] = ['a','b','c']
          
a
          
[0, 10, 'a', 30, 'b', 50, 'c', 70, 80, 90]
a = [0,10,20,30,40,50,60,70,80,90]
          
a[2:8:2] = ['a','b']
          
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    a[2:8:2] = ['a','b']
ValueError: attempt to assign sequence of size 2 to extended slice of size 3
b = (0,10,20,30,40,50,60,70,80,90)
          
b[2:5] = ('a','b','c')
          
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    b[2:5] = ('a','b','c')
TypeError: 'tuple' object does not support item assignment
a = [0,10,20,30,40,50,60,70,80,90]
          
del a[2:5]
          
a
          
[0, 10, 50, 60, 70, 80, 90]

# 연습문제
          
year = [2011,2012,2013,2014,2015,2016,2017,2018]
          
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
          
print(year[-3:])
          
[2016, 2017, 2018]
print(population[-3:])
          
[9930616, 9857426, 9838892]

# 연습문제2
          
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
          
print(n[::2])
          
(-32, 97, 9, 4, 0, 14)
print(n[1::2])
          
(75, -10, 32, -15, 76, 2)

# 심사문제1
          
x = input().split()
          
1 2 3 4 5 6 7 8 9 10
del x[-5:]
          
x
          
['1', '2', '3', '4', '5']
print(x)
          
['1', '2', '3', '4', '5']
x = input().split()
          
x = input().split()
x = input().split()
          
x = input().split()
x = input().split()
          
oven bat pony total leak wreck curl crop space navy loss knee
del x[-5:]
          
print(x)
          
['oven', 'bat', 'pony', 'total', 'leak', 'wreck', 'curl']
print(tuple(x))
          
('oven', 'bat', 'pony', 'total', 'leak', 'wreck', 'curl')

# 심사문제 2
          
a1 = input()
          
python
a2 = input()
          
python
print(a1[1::2] + a2[::2])
          
yhnpto
