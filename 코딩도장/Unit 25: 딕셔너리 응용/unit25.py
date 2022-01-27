# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

# 키와 기본값 저장
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault('e')
x
# {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None}

x.setdefault('f',100)
# 100
x
# {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None, 'f': 100}

# 키의 값 수정
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.update(a=90)
x
# {'a': 90, 'b': 20, 'c': 30, 'd': 40}
x.update(e=50)
x
# {'a': 90, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
x.update(a=900, f=60)
x
# {'a': 900, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}

y={1: 'one', 2: 'two'}
y.update({1:'ONE', 3: 'THREE'})
y
# {1: 'ONE', 2: 'two', 3: 'THREE'}
y.update([[2,'TWO'],[4,'FOUR']])
y
# {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR'}
y.update(zip([1,2],['one','two']))
y
# {1: 'one', 2: 'two', 3: 'THREE', 4: 'FOUR'}

# 키-값 쌍 삭제
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.pop('a')
# 10
x
# {'b': 20, 'c': 30, 'd': 40}
x.pop('z',0)
# 0

x = {'a':10, 'b':20, 'c':30, 'd':40}
del x['a']
x
# {'b': 20, 'c': 30, 'd': 40}

x = {'a':10, 'b':20, 'c':30, 'd':40}
x.popitem()
# ('d', 40)
x
# {'a': 10, 'b': 20, 'c': 30}

x = {'a':10, 'b':20, 'c':30, 'd':40}
x.clear()
x
# {}

# 키-값 가져오기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.get('a')
# 10
x.get('z',0)
# 0

x.items()
# dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
x.keys()
# dict_keys(['a', 'b', 'c', 'd'])
x.values()
# dict_values([10, 20, 30, 40])

# 리스트와 튜플로 딕셔너리 생성
keys=['a','b','c','d']
x=dict.fromkeys(keys)
x
# {'a': None, 'b': None, 'c': None, 'd': None}
y=dict.fromkeys(keys,100)
y
# {'a': 100, 'b': 100, 'c': 100, 'd': 100}

# defaultdict
from collections import defaultdict
y=defaultdict(int)
y['z']
# 0

z=defaultdict(lambda:'python')
z['a']
# 'python'
z[0]
# 'python'

# 딕셔너리 키-값 쌍 출력
x = {'a':10, 'b':20, 'c':30, 'd':40}
for i in x:
    print(i, end=' ')

    
# a b c d 

for key, value in x.items():
    print(key, value)

    
# a 10
# b 20
# c 30
# d 40

for key in x.keys():
    print(key, end=' ')

    
# a b c d 

for value in x.values():
    print(value, end=' ')

    
# 10 20 30 40 

# 딕셔너리 표현식
keys=['a','b','c','d']
x={key:value for key, value in dict.fromkeys(keys).items()}
x
# {'a': None, 'b': None, 'c': None, 'd': None}

{key:0 for key in dict.fromkeys(keys).keys()}
# {'a': 0, 'b': 0, 'c': 0, 'd': 0}

{value:0 for value in {'a':10, 'b': 20, 'c': 30, 'd':40}.values()}
# {10: 0, 20: 0, 30: 0, 40: 0}

{value: key for key, value in {'a':10, 'b': 20, 'c': 30, 'd': 40}.items()}
# {10: 'a', 20: 'b', 30: 'c', 40: 'd'}

x = {'a':10, 'b':20, 'c':30, 'd':40}
x = {key: value for key, value in x.items() if value!=20}
x
# {'a': 10, 'c': 30, 'd': 40}

# 중첩 딕셔너리
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
        
print(terrestrial_planet['Venus']['mean_radius'])      
# 6051.8

# 할당과 복사        
x = {'a':10, 'b':20, 'c':30, 'd':40}
y=x
x is y
True
y['a']=99
x
# {'a': 99, 'b': 20, 'c': 30, 'd': 40}
y
# {'a': 99, 'b': 20, 'c': 30, 'd': 40}

x = {'a':0, 'b':0, 'c':0, 'd':0}
y=x.copy()
x is y
# False
x==y
# True
y['a']=99
x
# {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y
# {'a': 99, 'b': 0, 'c': 0, 'd': 0}

x={'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy
y=copy.deepcopy(x)
y['a']['python']='2.7.15'
x
# {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y
# {'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}

# 연습문제
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}
average=sum(maria.values())/len(maria)
print(average)
# 89.25

# 심사문제
keys=input().split()
values=map(int, input().split())
x = dict(zip(keys, values))
x = {key: value for key, value in x.items() if key!='delta'}
x = {key: value for key, value in x.items() if value!=30}
print(x)

# alpha bravo charlie delta
# 10 20 30 40
# {'alpha': 10, 'bravo': 20}
