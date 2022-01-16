Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

for i in range(10):
    print('Hello, world!')

    
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!

for i in range(10):
    print('Hello, world!', i)

    
Hello, world! 0
Hello, world! 1
Hello, world! 2
Hello, world! 3
Hello, world! 4
Hello, world! 5
Hello, world! 6
Hello, world! 7
Hello, world! 8
Hello, world! 9

for i in range(5,12):
    print('Hello, world!', i)

    
Hello, world! 5
Hello, world! 6
Hello, world! 7
Hello, world! 8
Hello, world! 9
Hello, world! 10
Hello, world! 11

for i in range(0,10,2):
    print('Hello, world!', i)

    
Hello, world! 0
Hello, world! 2
Hello, world! 4
Hello, world! 6
Hello, world! 8

for i in range(10,0,-1):
    print('Hello, world!', i)

    
Hello, world! 10
Hello, world! 9
Hello, world! 8
Hello, world! 7
Hello, world! 6
Hello, world! 5
Hello, world! 4
Hello, world! 3
Hello, world! 2
Hello, world! 1

for i in reversed(range(10)):
    print('Hello, world!', i)

    
Hello, world! 9
Hello, world! 8
Hello, world! 7
Hello, world! 6
Hello, world! 5
Hello, world! 4
Hello, world! 3
Hello, world! 2
Hello, world! 1
Hello, world! 0

count = int(input('반복할 횟수를 입력하세요: '))
반복할 횟수를 입력하세요: 
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    count = int(input('반복할 횟수를 입력하세요: '))
ValueError: invalid literal for int() with base 10: ''
count = int(input('반복할 횟수를 입력하세요: '))
반복할 횟수를 입력하세요: 3
for i in range(count):
    print('Hello, world!', i)

    
Hello, world! 0
Hello, world! 1
Hello, world! 2

a = [10,20,30,40,50]
for i in a:
    print(i)

    
10
20
30
40
50

fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

    
apple
orange
grape

for letter in 'Python':
    print(letter, end = ' ')

    
P y t h o n 

for letter in reversed('Python'):
    print(letter, end = ' ')

    
n o h t y P 

# 연습문제
x = [49,-17,25,102,8,62,21]
for i in x:
    print(i*10, end = ' ')

    
490 -170 250 1020 80 620 210 

# 심사문제
count = int(input())
2
for i in range(1,10):
    print(count,' * ',i,' = ',count*i)

    
2  *  1  =  2
2  *  2  =  4
2  *  3  =  6
2  *  4  =  8
2  *  5  =  10
2  *  6  =  12
2  *  7  =  14
2  *  8  =  16
2  *  9  =  18
for i in range(1,10):
    print(count,'*',i,'=',count*i)

    
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
