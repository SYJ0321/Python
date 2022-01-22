# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

# 리스트에 요소 추가
a=[10,20,30]
a.append(500)
a
# [10, 20, 30, 500]

a=[]
a.append(10)
a
# [10]

a=[10,20,30]
a.append([500,600])
a
# [10, 20, 30, [500, 600]]
len(a)
# 4

# 리스트에 요소 여러 개 추가
a=[10,20,30]
a.extend([500,600])
a
# [10, 20, 30, 500, 600]
len(a)
# 5

# 리스트의 특정 인덱스에 요소 추가
a=[10,20,30]
a.insert(2,500)
a
# [10, 20, 500, 30]

a=[10,20,30]
a.insert(0,500)
a
# [500, 10, 20, 30]
a.insert(len(a),600)
a
# [500, 10, 20, 30, 600]

a=[10,20,30]
a.insert(1,[500,600])
a
# [10, [500, 600], 20, 30]

# 리스트 중간에 요소 여러 개 추가
a=[10,20,30]
a[1:1]=[500,600]
a
# [10, 500, 600, 20, 30]

# 리스트에서 특정 인덱스의 요소 삭제
a=[10,20,30]
a.pop()
# 30
a
# [10, 20]

a=[10,20,30]
a.pop(1)
# 20
a
# [10, 30]

# 리스트에서 특정 값을 찾아서 삭제
a=[10,20,30]
a.remove(20)
a
# [10, 30]

a=[10,20,30,20]
a.remove(20)
a
# [10, 30, 20]

# 덱
from collections import deque
a=deque([10,20,30])
a
# deque([10, 20, 30])
a.append(500)
a
# deque([10, 20, 30, 500])
a.popleft()
# 10
a
# deque([20, 30, 500])

# 특정 값의 인덱스 구하기
a=[10,20,30,15,20,40]
a.index(20)
# 1

# 특정 값의 개수 구하기
a=[10,20,30,15,20,40]
a.count(20)
# 2

# 리스트의 순서 뒤집기
a=[10,20,30,15,20,40]
a.reverse()
a
# [40, 20, 15, 30, 20, 10]

# 리스트의 요소 정렬
a=[10,20,30,15,20,40]
a.sort()
a
# [10, 15, 20, 20, 30, 40]
a.sort(reverse=True)
a
# [40, 30, 20, 20, 15, 10]

sorted(a)
# [10, 15, 20, 20, 30, 40]

# 리스트의 모든 요소 삭제
a=[10,20,30]
a.clear()
a
# []

# 리스트를 슬라이스로 조작하기
a=[10,20,30]
a[len(a):]=[500]
a
# [10, 20, 30, 500]

# 리스트의 할당
a=[0,0,0,0,0]
b=a

a is b
# True

b[2]=99
a
# [0, 0, 99, 0, 0]
b
# [0, 0, 99, 0, 0]

# 리스트의 복사
a=[0,0,0,0,0]
b=a.copy()

a is b
# False
a==b
# True

b[2]=99
a
# [0, 0, 0, 0, 0]
b
# [0, 0, 99, 0, 0]

# 반복문으로 리스트의 요소 출력하기
a=[38,21,53,62,19]
for i in a:
    print(i)

    
# 38
# 21
# 53
# 62
# 19

# 인덱스와 요소 함께 출력
a=[38,21,53,62,19]
for index, value in enumerate(a):
    print(index, value)

    
# 0 38
# 1 21
# 2 53
# 3 62
# 4 19

for index, value in enumerate(a):
    print(index+1, value)

    
# 1 38
# 2 21
# 3 53
# 4 62
# 5 19

for index, value in enumerate(a, start=1):
    print(index, value)

    
# 1 38
# 2 21
# 3 53
# 4 62
# 5 19

i=0
while i<len(a):
    print(a[i])
    i+=1

    
# 38
# 21
# 53
# 62
# 19

# 리스트의 가장 작은 수 찾기
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i

        
smallest
# 19

a.sort()
a[0]
# 19

a=[38,21,53,62,19]
min(a)
# 19

# 리스트의 가장 큰 수 찾기
largest=a[0]
for i in a:
    if i>largest:
        largest=i

        
largest
# 62

a.sort(reverse=True)
a[0]
# 62

a=[38,21,53,62,19]
max(a)
# 62

# 요소의 합계 구하기
a=[10,10,10,10,10]
x=0
for i in a:
    x+=i

    
x
# 50

sum(a)
# 50

# 리스트 표현식
a=[i for i in range(10)]
a
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b=list(i for i in range(10))
b
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

c=[i+5 for i in range(10)]
c
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

d=[i*2 for i in range(10)]
d
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

a = [i for i in range(10) if i%2==0]
a
# [0, 2, 4, 6, 8]

b = [i+5 for i in range(10) if i%2==1]
b
# [6, 8, 10, 12, 14]

a = [i*j for j in range(2,10) for i in range(1,10)]
a
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]

# 리스트에 map 사용하기
a=[1.2,2.5,3.7,4.6]
for i in range(len(a)):
    a[i]=int(a[i])

    
a
# [1, 2, 3, 4]

a=[1.2,2.5,3.7,4.6]
a=list(map(int,a))
a
# [1, 2, 3, 4]

a=list(map(str,range(10)))
a
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 튜플 메서드
a=(38,21,53,62,19,53)
a.index(53)
# 2
a.count(20)
# 0

for i in a:
    print(i, end=' ')

    
# 38 21 53 62 19 53 

a=tuple(i for i in range(10) if i%2==0)
a
# (0, 2, 4, 6, 8)

a=(1.2,2.5,3.7,4.6)
a=tuple(map(int,a))
a
# (1, 2, 3, 4)

a=(38,21,53,62,19,53)
min(a); max(a); sum(a)
# 19
# 62
# 246

# 연습문제
a=['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b=[i for i in a if len(i)==5]
print(b)
# ['alpha', 'bravo', 'delta', 'hotel', 'india']

# 심사문제
x,y=map(int,input().split())
a=[2**i for i in range(x,y+1)]
a.pop(1)
a.pop(-2)
print(a)
# 1 10
# [2, 8, 16, 32, 64, 128, 256, 1024]
