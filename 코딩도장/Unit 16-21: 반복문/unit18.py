# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

# break
i=0
while True:
    print(i)
    i += 1
    if i==10:
        break

    
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(100):
    print(i)
    if i==10:
        break

    
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
10

# continue
for i in range(10):
    if i%2==0:
        continue
    print(i)

    
# 1
# 3
# 5
# 7
# 9

i=0
while i<10:
    i+=1
    if i%2==0:
        continue
    print(i)

    
# 1
# 3
# 5
# 7
# 9

count = int(input('반복할 횟수를 입력하세요: '))
반복할 횟수를 입력하세요: 3
i=0
while True:
    print(i)
    i+=1
    if i==count:
        break

    
# 0
# 1
# 2

count = int(input('반복할 횟수를 입력하세요: '))
반복할 횟수를 입력하세요: 9
for i in range(count+1):
    if i%2==0:
        continue
    print(i)

    
# 1
# 3
# 5
# 7
# 9

# 연습문제
i=0
while True:
    if i%10!=3:
        i+=1
        continue
    if i>73:
        break
    print(i, end=' ')
    i+=1

    
# 3 13 23 33 43 53 63 73 

# 심사문제
start, stop = map(int, input().split())
i=start
while True:
    if i%10==3:
        i+=1
        continue
    if i>stop:
        break
    print(i, end=' ')
    i+=1


# 1 20
# 1 2 4 5 6 7 8 9 10 11 12 14 15 16 17 18 19 20 
