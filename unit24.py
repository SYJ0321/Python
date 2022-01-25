Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# 문자열 바꾸기
'Hello, world!'.replace('world', 'Python')
'Hello, Python!'

s='Hello, world!'
s=s.replace('world', 'Python')
s
'Hello, Python!'

# 문자 바꾸기
table=str.maketrans('aeiou', '12345')
'apple'.translate(table)
'1ppl2'

# 문자열 분리
'apple pear grape pineapple orange'.split()
['apple', 'pear', 'grape', 'pineapple', 'orange']

'apple, pear, grape, pineapple, orange'.split(',')
['apple', ' pear', ' grape', ' pineapple', ' orange']
'apple,pear,grape,pineapple,orange'.split(',')
['apple', 'pear', 'grape', 'pineapple', 'orange']

# 문자열 리스트 연결
' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
'apple pear grape pineapple orange'
','.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
'apple,pear,grape,pineapple,orange'

# 대소문자
'python'.upper()
'PYTHON'
'PYTHON'.lower()
'python'

# 공백 삭제
'   Python   '.lstrip()
'Python   '
'   Python   '.rstrip()
'   Python'
'   Python   '.strip()
'Python'

# 특정 문자 삭제
', python.'.lstrip(',.')
' python.'
', python.'.rstrip(',.')
', python'
', python.'.strip(',.')
' python'

import string
', python.'.strip(string.punctuation)
' python'
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
', python.'.strip(string.punctuation+' ')
'python'
', python.'.strip(string.punctuation).strip()
'python'

# 문자열 정렬
'python'.ljust(10)
'python    '
'python'.rjust(10)
'    python'
'python'.center(10)
'  python  '

# 메서드 체이닝
'python'.rjust(10).upper()
'    PYTHON'

# 문자열 왼쪽에 0 채우기
'35'.zfill(4)
'0035'
'3.5'.zfill(6)
'0003.5'
'hello'.zfill(10)
'00000hello'

# 문자열 위치 찾기
'apple pineapple'.find('pl')
2
'apple pineapple'.find('xy')
-1
'apple pineapple'.rfind('pl')
12
'apple pineapple'.rfind('xy')
-1
'apple pineapple'.index('pl')
2
'apple pineapple'.rindex('pl')
12

# 문자ㅕㅇㄹ 개수 세기
# 문자열 개수 세기
'apple pineapple'.count('pl')
2

# 서식 지정자
'I am %s.' % 'james'
'I am james.'

name = 'maria'
'I am %s.' % name
'I am maria.'

'I am %d years old.' % 20
'I am 20 years old.'

'%f' % 2.3
'2.300000'

'%.2f' % 2.3
'2.30'

'%10s' % 'python'
'    python'

'%10d'%150
'       150'
'%10.2f'%2.3
'      2.30'
'%-10s'%'python'
'python    '

'Today is %d %s' % (3, 'April')
'Today is 3 April'

# format 메서드
'Hello, {0}'.format('world!')
'Hello, world!'
'Hello, {0}'.format(100)
'Hello, 100'

'Hello, {0} {2} {1}'. format('Python', 'Script', 3.6)
'Hello, Python 3.6 Script'

'{0} {0} {1} {1}'.format('Python', 'Script')
'Python Python Script Script'

'Hello, {} {} {}'. format('Python', 'Script', 3.6)
'Hello, Python Script 3.6'

'Hello, {language} {version}'.format(language='Python', version=3.6)
'Hello, Python 3.6'

language='Python'
version=3.6
f'Hello, {language} {version}'
'Hello, Python 3.6'

'{{ {0} }}'.format('Python')
'{ Python }'

'{0:<10}'.format('python')
'python    '
'{0:>10}'.format('python')
'    python'

'{0:03d}'.format(35)
'035'

'{0:08.2f}'.format(150.37)
'00150.37'

'{0:0<10}'.format(15)
'1500000000'
'{0:0>10}'.format(15)
'0000000015'
'{0:0>10.2f}',format(15)
('{0:0>10.2f}', '15')
'{0:0>10.2f}'.format(15)
'0000015.00'
'{0: >10.2f}'.format(15)
'     15.00'
'{0:x>10.2f}'.format(15)
'xxxxx15.00'

# 금액에서 천단위로 콤마 넣기
format(1493500, ',')
'1,493,500'
'%20s' % format(1493500, ',')
'           1,493,500'
'{0:,}'.format(1493500)
'1,493,500'

# 연습문제
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
x
['C:', 'Users', 'dojang', 'AppData', 'Local', 'Programs', 'Python', 'Python36-32', 'python.exe']
filename = find('exe')
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    filename = find('exe')
NameError: name 'find' is not defined
filename = x[-1]
print(filename)
python.exe

# 심사문제1
x = input()
the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.
x
"the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
x.find('the')
0
x.count('the')
8
x.count('the ')
4
x=x.strip(string.punctuation)
x
"the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the"
x=x.strip(',')
x
"the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the"
x = input()
the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.

x
"the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
x.translate(str.maketrans('the', '789'))
"789 grown-ups' r9spons9, 78is 7im9, was 7o advis9 m9 7o lay asid9 my drawings of boa cons7ric7ors, w89789r from 789 insid9 or 789 ou7sid9, and d9vo79 mys9lf ins79ad 7o g9ograp8y, 8is7ory, ari78m97ic, and grammar. T8a7 is w8y, a7 789, ag9 of six, I gav9 up w8a7 mig87 8av9 b99n a magnific9n7 car99r as a pain79r. I 8ad b99n dis89ar79n9d by 789 failur9 of my Drawing Numb9r On9 and my Drawing Numb9r Two. Grown-ups n9v9r und9rs7and any78ing by 789ms9lv9s, and i7 is 7ir9som9 for c8ildr9n 7o b9 always and for9v9r 9xplaining 78ings 7o 789."
x
"the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
x.split()
['the', "grown-ups'", 'response,', 'this', 'time,', 'was', 'to', 'advise', 'me', 'to', 'lay', 'aside', 'my', 'drawings', 'of', 'boa', 'constrictors,', 'whether', 'from', 'the', 'inside', 'or', 'the', 'outside,', 'and', 'devote', 'myself', 'instead', 'to', 'geography,', 'history,', 'arithmetic,', 'and', 'grammar.', 'That', 'is', 'why,', 'at', 'the,', 'age', 'of', 'six,', 'I', 'gave', 'up', 'what', 'might', 'have', 'been', 'a', 'magnificent', 'career', 'as', 'a', 'painter.', 'I', 'had', 'been', 'disheartened', 'by', 'the', 'failure', 'of', 'my', 'Drawing', 'Number', 'One', 'and', 'my', 'Drawing', 'Number', 'Two.', 'Grown-ups', 'never', 'understand', 'anything', 'by', 'themselves,', 'and', 'it', 'is', 'tiresome', 'for', 'children', 'to', 'be', 'always', 'and', 'forever', 'explaining', 'things', 'to', 'the.']
y=x.split()
y
['the', "grown-ups'", 'response,', 'this', 'time,', 'was', 'to', 'advise', 'me', 'to', 'lay', 'aside', 'my', 'drawings', 'of', 'boa', 'constrictors,', 'whether', 'from', 'the', 'inside', 'or', 'the', 'outside,', 'and', 'devote', 'myself', 'instead', 'to', 'geography,', 'history,', 'arithmetic,', 'and', 'grammar.', 'That', 'is', 'why,', 'at', 'the,', 'age', 'of', 'six,', 'I', 'gave', 'up', 'what', 'might', 'have', 'been', 'a', 'magnificent', 'career', 'as', 'a', 'painter.', 'I', 'had', 'been', 'disheartened', 'by', 'the', 'failure', 'of', 'my', 'Drawing', 'Number', 'One', 'and', 'my', 'Drawing', 'Number', 'Two.', 'Grown-ups', 'never', 'understand', 'anything', 'by', 'themselves,', 'and', 'it', 'is', 'tiresome', 'for', 'children', 'to', 'be', 'always', 'and', 'forever', 'explaining', 'things', 'to', 'the.']
for i in y:
    i.strip(string.punctuation)

    
'the'
'grown-ups'
'response'
'this'
'time'
'was'
'to'
'advise'
'me'
'to'
'lay'
'aside'
'my'
'drawings'
'of'
'boa'
'constrictors'
'whether'
'from'
'the'
'inside'
'or'
'the'
'outside'
'and'
'devote'
'myself'
'instead'
'to'
'geography'
'history'
'arithmetic'
'and'
'grammar'
'That'
'is'
'why'
'at'
'the'
'age'
'of'
'six'
'I'
'gave'
'up'
'what'
'might'
'have'
'been'
'a'
'magnificent'
'career'
'as'
'a'
'painter'
'I'
'had'
'been'
'disheartened'
'by'
'the'
'failure'
'of'
'my'
'Drawing'
'Number'
'One'
'and'
'my'
'Drawing'
'Number'
'Two'
'Grown-ups'
'never'
'understand'
'anything'
'by'
'themselves'
'and'
'it'
'is'
'tiresome'
'for'
'children'
'to'
'be'
'always'
'and'
'forever'
'explaining'
'things'
'to'
'the'
for i in y:
    i=i.strip(string.punctuation)

    
y
['the', "grown-ups'", 'response,', 'this', 'time,', 'was', 'to', 'advise', 'me', 'to', 'lay', 'aside', 'my', 'drawings', 'of', 'boa', 'constrictors,', 'whether', 'from', 'the', 'inside', 'or', 'the', 'outside,', 'and', 'devote', 'myself', 'instead', 'to', 'geography,', 'history,', 'arithmetic,', 'and', 'grammar.', 'That', 'is', 'why,', 'at', 'the,', 'age', 'of', 'six,', 'I', 'gave', 'up', 'what', 'might', 'have', 'been', 'a', 'magnificent', 'career', 'as', 'a', 'painter.', 'I', 'had', 'been', 'disheartened', 'by', 'the', 'failure', 'of', 'my', 'Drawing', 'Number', 'One', 'and', 'my', 'Drawing', 'Number', 'Two.', 'Grown-ups', 'never', 'understand', 'anything', 'by', 'themselves,', 'and', 'it', 'is', 'tiresome', 'for', 'children', 'to', 'be', 'always', 'and', 'forever', 'explaining', 'things', 'to', 'the.']
for i in range(len(y)):
    y[i]=y[i].strip(string.punctuation)

    
y
['the', 'grown-ups', 'response', 'this', 'time', 'was', 'to', 'advise', 'me', 'to', 'lay', 'aside', 'my', 'drawings', 'of', 'boa', 'constrictors', 'whether', 'from', 'the', 'inside', 'or', 'the', 'outside', 'and', 'devote', 'myself', 'instead', 'to', 'geography', 'history', 'arithmetic', 'and', 'grammar', 'That', 'is', 'why', 'at', 'the', 'age', 'of', 'six', 'I', 'gave', 'up', 'what', 'might', 'have', 'been', 'a', 'magnificent', 'career', 'as', 'a', 'painter', 'I', 'had', 'been', 'disheartened', 'by', 'the', 'failure', 'of', 'my', 'Drawing', 'Number', 'One', 'and', 'my', 'Drawing', 'Number', 'Two', 'Grown-ups', 'never', 'understand', 'anything', 'by', 'themselves', 'and', 'it', 'is', 'tiresome', 'for', 'children', 'to', 'be', 'always', 'and', 'forever', 'explaining', 'things', 'to', 'the']
num=0
for i in y:
    if i=='the':
        num+=1

        
num
6
for i in y:
    if i=='the':
        nt+=1

        
Traceback (most recent call last):
  File "<pyshell#166>", line 3, in <module>
    nt+=1
NameError: name 'nt' is not defined. Did you mean: 'int'?
x=input().split()
x=input().split()
the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.
num=0
for i in range(len(x)):
    x[i]=x[i].strip(string.punctuation)
    if x[i]=='the':
        num+=1

        
num
6
print(num)
6
x=input().split()
the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.
x
['the', "grown-ups'", 'response,', 'this', 'time,', 'was', 'to', 'advise', 'me', 'to', 'lay', 'aside', 'my', 'drawings', 'of', 'boa', 'constrictors,', 'whether', 'from', 'the', 'inside', 'or', 'the', 'outside,', 'and', 'devote', 'myself', 'instead', 'to', 'geography,', 'history,', 'arithmetic,', 'and', 'grammar.', 'That', 'is', 'why,', 'at', 'the,', 'age', 'of', 'six,', 'I', 'gave', 'up', 'what', 'might', 'have', 'been', 'a', 'magnificent', 'career', 'as', 'a', 'painter.', 'I', 'had', 'been', 'disheartened', 'by', 'the', 'failure', 'of', 'my', 'Drawing', 'Number', 'One', 'and', 'my', 'Drawing', 'Number', 'Two.', 'Grown-ups', 'never', 'understand', 'anything', 'by', 'themselves,', 'and', 'it', 'is', 'tiresome', 'for', 'children', 'to', 'be', 'always', 'and', 'forever', 'explaining', 'things', 'to', 'the.']
num=0
for i in range(len(x)):
    x[i]=x[i].strip(string.punctuation)
    if x[i]=='the':
        num+=1

        
num
6
x
['the', 'grown-ups', 'response', 'this', 'time', 'was', 'to', 'advise', 'me', 'to', 'lay', 'aside', 'my', 'drawings', 'of', 'boa', 'constrictors', 'whether', 'from', 'the', 'inside', 'or', 'the', 'outside', 'and', 'devote', 'myself', 'instead', 'to', 'geography', 'history', 'arithmetic', 'and', 'grammar', 'That', 'is', 'why', 'at', 'the', 'age', 'of', 'six', 'I', 'gave', 'up', 'what', 'might', 'have', 'been', 'a', 'magnificent', 'career', 'as', 'a', 'painter', 'I', 'had', 'been', 'disheartened', 'by', 'the', 'failure', 'of', 'my', 'Drawing', 'Number', 'One', 'and', 'my', 'Drawing', 'Number', 'Two', 'Grown-ups', 'never', 'understand', 'anything', 'by', 'themselves', 'and', 'it', 'is', 'tiresome', 'for', 'children', 'to', 'be', 'always', 'and', 'forever', 'explaining', 'things', 'to', 'the']
num=0
for i in range(len(x)):
    x[i]=x[i].strip(',.')
    if x[i]=='the':
        num+=1

        
print(num)
6

# 심사문제2
price=input.split(';')
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    price=input.split(';')
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
price=input().split(';')
51900;83000;158000;367500;250000;59200;128500;1304000
price
['51900', '83000', '158000', '367500', '250000', '59200', '128500', '1304000']
price=map(int,input().split(';'))
51900;83000;158000;367500;250000;59200;128500;1304000
price
<map object at 0x0000017B4524A8F0>
print(price)
<map object at 0x0000017B4524A8F0>
price=sort(price, reverse=True)
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    price=sort(price, reverse=True)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
sort(price, reverse=True)
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    sort(price, reverse=True)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
price=sorted(price, reverse=True)
price
[1304000, 367500, 250000, 158000, 128500, 83000, 59200, 51900]
price.rjust(9)
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    price.rjust(9)
AttributeError: 'list' object has no attribute 'rjust'
price=input().split(';')
51900;83000;158000;367500;250000;59200;128500;1304000
price=sorted(price, reverse=True)
price
['83000', '59200', '51900', '367500', '250000', '158000', '1304000', '128500']
price=map(int,input().split(';'))
51900;83000;158000;367500;250000;59200;128500;1304000
price=sorted(price, reverse=True)
pric
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    pric
NameError: name 'pric' is not defined. Did you mean: 'price'?
e
price
[1304000, 367500, 250000, 158000, 128500, 83000, 59200, 51900]
format(price,',')
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    format(price,',')
TypeError: unsupported format string passed to list.__format__
price.format(',')
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    price.format(',')
AttributeError: 'list' object has no attribute 'format'
for i in price:
    print(i)

    
1304000
367500
250000
158000
128500
83000
59200
51900
for i in price:
    print(format(i,',').rjust(9))

    
1,304,000
  367,500
  250,000
  158,000
  128,500
   83,000
   59,200
   51,900
