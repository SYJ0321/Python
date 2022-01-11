# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux
# {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

# 중복된 키는 저장 X
lux = {'health': 490, 'health': 900, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health']
# 900
lux
# {'health': 900, 'mana': 334, 'melee': 550, 'armor': 18.72}

x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
x
# {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}

# 키에는 리스트, 딕셔너리 사용 불가
x = {[10,20]: 100}
# Traceback (most recent call last):
#   File "<pyshell#11>", line 1, in <module>
#     x = {[10,20]: 100}
# TypeError: unhashable type: 'list'

x = {{'a':10}: 100}
# Traceback (most recent call last):
#   File "<pyshell#12>", line 1, in <module>
#     x = {{'a':10}: 100}
# TypeError: unhashable type: 'dict'

# 빈 딕셔너리
x = {}
x
# {}

y = dict()
y
# {}

# dict()
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux1
# {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
lux2
# {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux3
# {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})    
lux4
# {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

# 키에 접근하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health']       
# 490
lux['armor']          
# 18.72

# 키에 값 할당하기    
lux['health'] = 2037
lux['mana'] = 1184  
lux
# {'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72}

# 없는 키에 값을 할당하면 새로운 키 생성 & 값 할당
lux['mana_regen'] = 3.28
lux
# {'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72, 'mana_regen': 3.28}

'health' in lux           
# True
'attack_speed' not in lux          
# True

len(lux)
# 5

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
print(camille['movement_speed'])
# 575.6            
# 340

# 심사문제
key = input().split()
val = map(float, input().split())
dt = dict(zip(key, val))
print(dt)
# health health_regen mana mana_regen  
# 574.6 1.7 338.8 1.63
# {'health': 574.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}
