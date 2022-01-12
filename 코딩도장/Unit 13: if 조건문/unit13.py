Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=10
if x==10:
    print('10입니다.')

    
10입니다.

# pass
if x==10:
    pass # TODO: x가 10일 때 처리 필요

x=10
if x==10:
    print('x에 들어있는 숫자는')
    print('10입니다.')

    
x에 들어있는 숫자는
10입니다.

x=5
if x==10:
    print('x에 들어있는 숫자는')
print('10입니다.')
SyntaxError: invalid syntax

x=15
if x>=10:
    print('10 이상입니다.')

    
10 이상입니다.
x=15
if x>=10:
    print('10 이상입니다.')
    if x==15:
        print('15입니다.')
    if x==20:
        print('20입니다.')

        
10 이상입니다.
15입니다.

x = int(input())
10
if x==10:
    print('10입니다.')

    
10입니다.
if x==20:
    print('20입니다.')

    
# 연습문제
x=5
if x!=10:
    print('ok')

    
ok

# 심사문제
price = int(input())
27000
name = input()
Cash3000
if name == 'Cash3000':
    print(price-3000)

    
24000
if name == 'Cash5000':
    print(price-5000)

    
if name == 'Cash3000':
    sale = price-3000

    
if name == 'Cash5000':
    sale = price-5000

    
print(sale)
24000
