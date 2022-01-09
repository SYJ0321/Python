# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

a = [38, 21,53, 62,19]
a
# [38, 21, 53, 62, 19]

person = ['james', 17, 175.3, True]
person
# ['james', 17, 175.3, True]

# 빈 리스트
a = []
a
# []
b = list()
b
# []

# range()
a = list(range(10))
a
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = list(range(5,12))
b
# [5, 6, 7, 8, 9, 10, 11]

c = list(range(-4,10,2))
c
# [-4, -2, 0, 2, 4, 6, 8]

d = list(range(10,0,-1))
d
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 튜플
a = (38, 21, 53, 62, 19)
a
# (38, 21, 53, 62, 19)

a = 38, 21, 53, 62, 19
a
# (38, 21, 53, 62, 19)

person = ('james', 17, 175.3, True)
person
# ('james', 17, 175.3, True)

(38, )
# (38,)
38,
# (38,)

tuple(range(10))
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# 리스트 -> 튜플
a = [1,2,3]
tuple(a)
# (1, 2, 3)

# 튜플 -> 리스트
b = (4,5,6)
list(b)
# [4, 5, 6]

# 문자열 -> 리스트/튜플
list('Hello')
# ['H', 'e', 'l', 'l', 'o']
tuple('Hello')
# ('H', 'e', 'l', 'l', 'o')

# 리스트/튜플로 값 할당
a, b, c = [1, 2, 3]
print(a,b,c)
# 1 2 3
d, e, f = (4, 5, 6)
print(d,e,f)
# 4 5 6

# 연습문제
a = list(range(5,-11,-2))
print(a)
# [5, 3, 1, -1, -3, -5, -7, -9]

# 심사문제
x = int(input())
tup = tuple(range(-10,10,x))
print(tup)
# 2
# (-10, -8, -6, -4, -2, 0, 2, 4, 6, 8)
