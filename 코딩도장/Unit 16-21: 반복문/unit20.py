# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

# 1부터 100까지 출력하기
for i in range(1,101):
    print(i, end=' ')

    
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 

# 3의 배수와 5의 배수 처리
for i in range(1,101):
    if i%3==0:
        print('Fizz', end=' ')
    elif i%5==0:
        print('Buzz', end=' ')
    else:
        print(i, end=' ')

        
# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 Fizz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 Fizz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 Fizz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 Fizz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 Fizz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz 

# 3과 5의 공배수 처리
for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

        
# 1
# 2
# Fizz
# ...
# 98
# Fizz
# Buzz

# 논리 연산자를 사용하지 않는 방법
for i in range(1,101):
    if i%15==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

        
# 1
# 2
# Fizz
# ...
# 98
# Fizz
# Buzz

# 코드 단축하기
for i in range(1,101):
    print('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or i)

    
# 1
# 2
# Fizz
# ...
# 98
# Fizz
# Buzz

# 연습문제
for i in range(1,101):
    if i%2==0 and i%11==0:
        print('FizzBuzz')
    elif i%2==0:
        print('Fizz')
    elif i%11==0:
        print('Buzz')
    else:
        print(i)

        
# 1
# Fizz
# 3
# ...
# Fizz
# Buzz
# Fizz

# 심사문제
x,y=map(int, input().split())
for i in range(x,y+1):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)

# 35 40        
# FizzBuzz
# 36
# 37
# 38
# 39
# Fizz
