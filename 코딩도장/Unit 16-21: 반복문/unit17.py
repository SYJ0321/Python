# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

i=0
while i<10:
    print('Hello, world!')
    i += 1

    
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!

i=1
while i<=10:
    print('Hello, world!', i)
    i+=1

    
# Hello, world! 1
# Hello, world! 2
# Hello, world! 3
# Hello, world! 4
# Hello, world! 5
# Hello, world! 6
# Hello, world! 7
# Hello, world! 8
# Hello, world! 9
# Hello, world! 10

i=10
while i>0:
    print('Hello, world!', i)
    i -= 1

    
# Hello, world! 10
# Hello, world! 9
# Hello, world! 8
# Hello, world! 7
# Hello, world! 6
# Hello, world! 5
# Hello, world! 4
# Hello, world! 3
# Hello, world! 2
# Hello, world! 1

count=int(input('반복할 횟수를 입력하세요: '))
i=0
while i<count:
    print('Hello, world!', i)
    i+=1

# 반복할 횟수를 입력하세요: 3    
# Hello, world! 0
# Hello, world! 1
# Hello, world! 2

count=int(input('반복할 횟수를 입력하세요: '))
while count > 0:
    print('Hello, world!', count)
    count -= 1

# 반복할 횟수를 입력하세요: 3   
# Hello, world! 3
# Hello, world! 2
# Hello, world! 1

# random 모듈
import random
random.random()
# 0.8484731822764804
random.randint(1,6)
# 4

i=0
while i!=3:
    i=random.randint(1,6)
    print(i)

    
# 2
# 1
# 5
# 6
# 2
# 3

dice = [1,2,3,4,5,6]
random.choice(dice)
# 1
random.choice(dice)
# 6

# 무한루프
# while True:
#     print('Hello, world!')


# 연습문제
i=2; j=5
while i<=32 or j>=1:
    print(i,j)
    i*=2
    j-=1

    
# 2 5
# 4 4
# 8 3
# 16 2
# 32 1

# 심사문제
money = int(input())
while money>=1350:
    money-=1350
    print(money)

# 10000    
# 8650
# 7300
# 5950
# 4600
# 3250
# 1900
# 550
