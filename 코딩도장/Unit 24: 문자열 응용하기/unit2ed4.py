# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

# 문자열 바꾸기
'Hello, world!'.replace('world', 'Python')
# 'Hello, Python!'

s='Hello, world!'
s=s.replace('world', 'Python')
s
# 'Hello, Python!'

# 문자 바꾸기
table=str.maketrans('aeiou', '12345')
'apple'.translate(table)
# '1ppl2'

# 문자열 분리
'apple pear grape pineapple orange'.split()
# ['apple', 'pear', 'grape', 'pineapple', 'orange']

'apple,pear,grape,pineapple,orange'.split(',')
# ['apple', 'pear', 'grape', 'pineapple', 'orange']

# 문자열 리스트 연결
' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
# 'apple pear grape pineapple orange'
','.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
# 'apple,pear,grape,pineapple,orange'

# 대소문자
'python'.upper()
# 'PYTHON'
'PYTHON'.lower()
# 'python'

# 공백 삭제
'   Python   '.lstrip()
# 'Python   '
'   Python   '.rstrip()
# '   Python'
'   Python   '.strip()
# 'Python'

# 특정 문자 삭제
', python.'.lstrip(',.')
# ' python.'
', python.'.rstrip(',.')
# ', python'
', python.'.strip(',.')
# ' python'

import string
', python.'.strip(string.punctuation)
# ' python'
string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

', python.'.strip(string.punctuation+' ')
# 'python'
', python.'.strip(string.punctuation).strip()
# 'python'

# 문자열 정렬
'python'.ljust(10)
# 'python    '
'python'.rjust(10)
# '    python'
'python'.center(10)
# '  python  '

# 메서드 체이닝
'python'.rjust(10).upper()
# '    PYTHON'

# 문자열 왼쪽에 0 채우기
'35'.zfill(4)
# '0035'
'3.5'.zfill(6)
# '0003.5'
'hello'.zfill(10)
# '00000hello'

# 문자열 위치 찾기
'apple pineapple'.find('pl')
# 2
'apple pineapple'.find('xy')
# -1
'apple pineapple'.rfind('pl')
# 12
'apple pineapple'.rfind('xy')
# -1

'apple pineapple'.index('pl')
# 2
'apple pineapple'.rindex('pl')
# 12

# 문자열 개수 세기
'apple pineapple'.count('pl')
# 2

# 서식 지정자
'I am %s.' % 'james'
# 'I am james.'

name = 'maria'
'I am %s.' % name
# 'I am maria.'

'I am %d years old.' % 20
# 'I am 20 years old.'

'%f' % 2.3
# '2.300000'

'%.2f' % 2.3
# '2.30'

'%10s' % 'python'
# '    python'
'%10d'%150
# '       150'
'%10.2f'%2.3
# '      2.30'
'%-10s'%'python'
# 'python    '

'Today is %d %s' % (3, 'April')
# 'Today is 3 April'

# format 메서드
'Hello, {0}'.format('world!')
# 'Hello, world!'
'Hello, {0}'.format(100)
# 'Hello, 100'

'Hello, {0} {2} {1}'. format('Python', 'Script', 3.6)
# 'Hello, Python 3.6 Script'

'{0} {0} {1} {1}'.format('Python', 'Script')
# 'Python Python Script Script'

'Hello, {} {} {}'. format('Python', 'Script', 3.6)
# 'Hello, Python Script 3.6'

'Hello, {language} {version}'.format(language='Python', version=3.6)
# 'Hello, Python 3.6'

language='Python'
version=3.6
f'Hello, {language} {version}'
# 'Hello, Python 3.6'

'{{ {0} }}'.format('Python')
# '{ Python }'

'{0:<10}'.format('python')
# 'python    '
'{0:>10}'.format('python')
# '    python'

'{0:03d}'.format(35)
# '035'

'{0:08.2f}'.format(150.37)
# '00150.37'

'{0:0<10}'.format(15)
# '1500000000'
'{0:0>10}'.format(15)
# '0000000015'
'{0:0>10.2f}'.format(15)
# '0000015.00'
'{0: >10.2f}'.format(15)
# '     15.00'
'{0:x>10.2f}'.format(15)
# 'xxxxx15.00'

# 금액에서 천단위로 콤마 넣기
format(1493500, ',')
# '1,493,500'
'%20s' % format(1493500, ',')
# '           1,493,500'
'{0:,}'.format(1493500)
# '1,493,500'

# 연습문제
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
filename = x[-1]
print(filename)
# python.exe

# 심사문제1
x=input().split()
num=0
for i in range(len(x)):
    x[i]=x[i].strip(',.')
    if x[i]=='the':
        num+=1

        
print(num)
# the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.
# 6

# 심사문제2
price=map(int,input().split(';'))
price=sorted(price, reverse=True)
for i in price:
    print(format(i,',').rjust(9))


# 51900;83000;158000;367500;250000;59200;128500;1304000
# 1,304,000
#   367,500
#   250,000
#   158,000
#   128,500
#    83,000
#    59,200
#    51,900
