# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')

    
# j:0 j:1 j:2 j:3 j:4 i:0\n
# j:0 j:1 j:2 j:3 j:4 i:1\n
# j:0 j:1 j:2 j:3 j:4 i:2\n
# j:0 j:1 j:2 j:3 j:4 i:3\n
# j:0 j:1 j:2 j:3 j:4 i:4\n

# 사각형으로 별 출력하기
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

    
# *****
# *****
# *****
# *****
# *****

for i in range(3):
    for j in range(7):
        print('*', end='')
    print()

    
# *******
# *******
# *******

# 계단식으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j<=i:
            print('*', end='')
    print()

    
# *
# **
# ***
# ****
# *****

# 대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j==i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

    
# *    
#  *   
#   *  
#    * 
#     *

# 연습문제
for i in range(5):
    for j in range(5):
        if j<i:
            print(' ', end='')
        else:
            print('*', end='')
    print()

    
# *****
#  ****
#   ***
#    **
#     *

# 심사문제
height = int(input())
for i in range(height):
    for j in range(2*height+1):
        if j<height-i-1:
            print(' ', end='')
        elif j>height+i-1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

    
# 3
#   *    
#  ***   
# *****  
