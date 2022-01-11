Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

# 중복된 키는 저장 X
lux = {'health': 490, 'health': 900, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health']
900
lux
{'health': 900, 'mana': 334, 'melee': 550, 'armor': 18.72}

x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
x
{100: 'hundred', False: 0, 3.5: [3.5, 3.5]}

x = {[10,20]: 100}
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x = {[10,20]: 100}
TypeError: unhashable type: 'list'
x = {{'a':10}: 100}
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x = {{'a':10}: 100}
TypeError: unhashable type: 'dict'

# 빈 딕셔너리
x = {}
x
{}
y = dict()
y
{}

# dict()
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux1
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
lux2
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux3
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72'})
             
SyntaxError: unterminated string literal (detected at line 1)
lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
             
lux4
             
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

# 키에 접근하기
             
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
             
lux['health']
             
490
lux['armor']
             
18.72

# 키에 값 할당하기
             
lux['health'] = 2037
             
lux['mana'] = 1184
             
lux
             
{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72}

lux['mana_regen'] = 3.28
             
lux
             
{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72, 'mana_regen': 3.28}

'health' in lux
             
True
'attack_speed' not in lux
             
True
len(lux)
             
5

# 연습문제
             
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
    }
             
print(camille['health'])
             
575.6
print(camille['movement_speed'])
             
340

# 심사문제
             
key = input().split()
             
health health_regen mana mana_regen
val = input().split()
             
575.6 1.7 338.8 1.63
key
             
['health', 'health_regen', 'mana', 'mana_regen']
val
             
['575.6', '1.7', '338.8', '1.63']
val = map(int, input().split())
             
575.6 1.7 338.8 1.63
val
             
<map object at 0x0000016C92FEB940>
val
             
<map object at 0x0000016C92FEB940>
val = map(int, input().split())
             
575.6 1.7 338.8 1.63
val
             
<map object at 0x0000016C92FE9FF0>
del val
             
val
             
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    val
NameError: name 'val' is not defined. Did you mean: 'eval'?
val = map(int, input().split())
             
575.6 1.7 338.8 1.63
val
             
<map object at 0x0000016C92FE9F90>
val = map(float, input().split())
             
575.6 1.7 338.81.63
val
             
<map object at 0x0000016C92FE9DE0>
val = map(int, input().split())
             
575.6 1.7 338.8 1.63
val
             
<map object at 0x0000016C92FE9FF0>
val = map(float, input().split())
             
575.6 1.7 338.8 1.63
val
             
<map object at 0x0000016C92FE9F90>
val = float(input().split())
             
575.6 1.7 338.8 1.63
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    val = float(input().split())
TypeError: float() argument must be a string or a real number, not 'list'
val = input().split()
             
575.6 1.7 338.8 1.63
val
             
['575.6', '1.7', '338.8', '1.63']
float(val)
             
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    float(val)
TypeError: float() argument must be a string or a real number, not 'list'
dict(zip(key,val))
             
{'health': '575.6', 'health_regen': '1.7', 'mana': '338.8', 'mana_regen': '1.63'}
val = map(float, input().split())
             
575.6 1.7 338.8 1.63
val
             
<map object at 0x0000016C92FEBAC0>
dict(zip(key,val))
             
{'health': 575.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}
dt = dict(zip(key,val))
             
print(dt)
             
{}
print(dt)
             
{}
dt
             
{}
dt = dict(zip(key,val))
             
dt
             
{}
dict(zip(key,val))
             
{}
key
             
['health', 'health_regen', 'mana', 'mana_regen']
val
             
<map object at 0x0000016C92FEBAC0>
dict(zip(key,val))
             
{}
del key
             
del val
             
del dy
             
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    del dy
NameError: name 'dy' is not defined. Did you mean: 'y'?
del dt
             
key = input().split()
             
'health' 'healt_regen' 'mana' 'mana_regen'
key
             
["'health'", "'healt_regen'", "'mana'", "'mana_regen'"]
del key
             
key = input().split()
             
health health_regen mana mana_regen
key
             
['health', 'health_regen', 'mana', 'mana_regen']
val = map(float, input().split())
             
574.6 1.7 338.8 1.63
val
             
<map object at 0x0000016C92FEB5B0>
dt = dict(zip(key, val))
             
dt
             
{'health': 574.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}
print(dt)
             
{'health': 574.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}
