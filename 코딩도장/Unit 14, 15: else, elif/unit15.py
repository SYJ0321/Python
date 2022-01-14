Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

x=20
if x==10:
    print('10입니다.')
elif x==20:
    print('20입니다.')

    
20입니다.

x=30
if x==10:
    print('10입니다.')
elif x==20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')

    
10도 20도 아닙니다.

# 음료수 자판기 만들기
button = int(input())
1
if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')

    
콜라

# 연습문제
x = int(input())
5
if 11<=x<=20:
    print('11~20')
elif 21<=x<=30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

    
아무것도 해당하지 않음

# 심사문제
age = int(input())
17
balance = 9000
if 7 <= age <= 12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
elif age >= 19:
    balance -= 1250

    
print(balance)
7950
