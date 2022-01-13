Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

x=5
if x==10:
    print('10입니다.')
else:
    print('10이 아닙니다.')

    
10이 아닙니다.

# 조건부 표현식
x=5
y=x if x==10 else 0
y
0

if True:
    print('참')
else:
    print('거짓')

    
참
if False:
    print('참')
else:
    print('거짓')

    
거짓
if None:
    print('참')
else:
    print('거짓')

    
거짓

if 0:
    print('참')
else:
    print('거짓')

    
거짓
if 1:
    print('참')
else:
    print('거짓')

    
참
if 0x1F:
    print('참')
else:
    print('거짓')

    
참
if 13.5:
    print('참')
else:
    print('거짓')

    
참

if 'Hello':
    print('참')
else:
    print('거짓')

    
참
if '':
    print('참')
else:
    print('거짓')

    
거짓
if not 0:
    print('참')

    
참
if not None:
    print('참')

    
참
if not '':
    print('참')

    
참

# 조건식 여러 개 지정하기
x=10; y=20
if x==10 and y==20:
    print('참')
else:
    print('거짓')

    
참

if 0<x<20:
    print('20보다 작은 양수입니다.')

    
20보다 작은 양수입니다.

# 연습문제
written_test = 75
coding_test = True
if written_test>=80 and coding_test==True:
    print('합격')
else:
    print('불합격')

    
불합격

# 심사문제
kor, eng, mat, sci = map(int, input().split())
89 72 93 82
if 0<kor,eng<100:
    
SyntaxError: invalid syntax
if 0<=kor<=100 and 0<=eng<=100 and 0<=mat<=100 and 0<=sci<=100:
    avg = (kor+eng+mat+sci)/4
    if avg>=80:
        print('합격')
    else:
        print('불합격')

        
합격
if 0<=kor<=100 and 0<=eng<=100 and 0<=mat<=100 and 0<=sci<=100:
    if (kor+eng+mat+sci)/4>=80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')

    
합격
