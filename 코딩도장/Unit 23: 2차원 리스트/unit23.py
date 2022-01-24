Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

a = [[10,20], [30,40], [50,60]]
a
[[10, 20], [30, 40], [50, 60]]
a[0][0]
10
a[1][1]
40
a[0][1]=1000
a
[[10, 1000], [30, 40], [50, 60]]

# 톱니형 리스트
a = [[10,20],
     [500,600,700],
     [9],
     [30,40],
     [8],
     [800,900,1000]]

a = []
a.append([])
a
[[]]
a[0].append(10); a[0].append(20)
a
[[10, 20]]
a.append([])
a[1].append(500); a[1].append(600); a[1].append(700)
a
[[10, 20], [500, 600, 700]]

# 2차원 튜플
a = ((10,20), (30,40), (50,60))
b = ([10,20], [30,40], [50,60])
c = [(10,20), (30,40), (50,60)]

a = [[10,20], [30,40], [50,60]]
from pprint import pprint
pprint(a, indent=4, width=20)
[   [10, 20],
    [30, 40],
    [50, 60]]

# 반복문으로 요소 모두 출력하기
for x,y in a:
    print(x,y)

    
10 20
30 40
50 60

for i in a:
    for j in i:
        print(j, end=' ')
    print()

    
10 20 
30 40 
50 60 

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

    
10 20 
30 40 
50 60 

i=0
while i<len(a):
    x,y=a[i]
    print(x,y)
    i+=1

    
10 20
30 40
50 60

i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j], end=' ')
        j+=1
    print()
    i+=1

    
10 20 
30 40 
50 60 

# 반복문으로 리스트 만들기
a=[]
for i in range(10):
    a.append(0)

    
print(a)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

a=[]
for i in range(30:
               
SyntaxError: expected ':'
for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)

            
print(a)
               
[[0, 0], [0, 0], [0, 0]]

a = [[0 for j in range(2) for i in range(3)]]
               
a = [[0 for j in range(2)] for i in range(3)]
               
a
               
[[0, 0], [0, 0], [0, 0]]

a = [[0]*2 for i in range(3)]
               
a
               
[[0, 0], [0, 0], [0, 0]]

a = [3,1,3,2,5]
               
b=[]
               
for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)

               
print(b)
               
[[0, 0, 0], [0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]]

a = [[0]*i for i in [3,1,3,2,5]]
               
a
               
[[0, 0, 0], [0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]]

# 2차원 리스트 정렬하기
               
students=[
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]
               
print(sorted(students, key=lambda student: student[1]))
               
[['maria', 'A', 25], ['andrew', 'B', 7], ['john', 'C', 19]]
print(sorted(students, key=lambda student: student[2]))
               
[['andrew', 'B', 7], ['john', 'C', 19], ['maria', 'A', 25]]

# 2차원 리스트의 할당과 복사
               
a=[10,20], [30,40]]
SyntaxError: unmatched ']'
a=[[10,20], [30,40]]
b=a
b[0][0]=500
a
[[500, 20], [30, 40]]
b
[[500, 20], [30, 40]]

a=[[10,20], [30,40]]
b=a.copy()
b[0][0]=500
a
[[500, 20], [30, 40]]
b
[[500, 20], [30, 40]]

a=[[10,20], [30,40]]
import copy
b=copy.deepcopy(a)
b[0][0]=500
a
[[10, 20], [30, 40]]
b
[[500, 20], [30, 40]]

# 연습문제
a = [[[0 for i in range(3)] for j in range(4)] for k in range(2)]
print(a)
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]

# 지뢰찾기
col, row = map(int, input().split())
3 3
matri=[]
for i in range(row):
    matrix.append(list(input()))
    .**
    
SyntaxError: invalid syntax
for i in range(row):
    matrix.append(list(input()))

    
Traceback (most recent call last):
  File "<pyshell#155>", line 2, in <module>
    matrix.append(list(input()))
NameError: name 'matrix' is not defined. Did you mean: 'matri'?
matrix=[]
for i in range(row):
    matrix.append(list(input()))

    

.**
*..
matrix
[[], ['.', '*', '*'], ['*', '.', '.']]
matrix=[]
for i in range(row):
    matrix.append(list(input()))

    
.**
*..
.*.
matrix
[['.', '*', '*'], ['*', '.', '.'], ['.', '*', '.']]
for i in range(row):
    for j in range(col):
        if j==0:
            if matrix[i][j+1]=='*'
            
SyntaxError: expected ':'
new = [[0 for i in range(row)] for j in range(col)]
new
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
forfor i in range(row):
    for j in range(col):
        if j==0:
            if matrix[i][j+1]=='*':
                
SyntaxError: invalid syntax
forfor i in range(row):
    for j in range(col):
        if j==0:
            if matrix[i][j+1]=='*':
                
SyntaxError: invalid syntax
for i in range(row):
    for j in range(col):
        if j==0:
            if matrix[i][j+1]=='*':
                new[i][j]+=1
            if matrix[i+1][j]=='*':
                new[i][j]+=1
        if j==row-1:
            if matrix[i][j-1]=='*':
                new[i][j]+=1
            if matrix[i+1][j]=='*'
            
SyntaxError: expected ':'
for i in range(row):
    for j in range(col):
        if i==0:
            if j==0:
                if matrix[i][j+1]=='*':
                    new[i][j]+=1
                if matrix[i+1][j]=='*':
                    new[i][j]+=1
            elif j==row-1:
                if matrix[i][j-1]=='*':
                    new[i][j]+=1
                if matrix[i+1][j]=='*':
                    new[i][j]+=1
            else:
                if matrix[i][j+1]=='*':
                    new[i][j]+=1
                if matrix[i][j-1]=='*':
                    new[i][j]+=1
                if matrix[i+1][j]=='*':
                    new[i][j]+=1

                    

new
[[2, 1, 1], [0, 0, 0], [0, 0, 0]]
for i in range(row):
    for j in rang(col):
        if matrix[i][j]=='*':
            new[i][j]=='*'
        else:
            if matrix[i-1][j]=='*':
                new[i][j]+=1
            if matrix[i+1][j]=='*':
                new[i][j]+=1
            if matrix[i][j-1]=='*':
                new=[i][j]+=1
                
SyntaxError: invalid syntax
for i in range(row):
    for j in rang(col):
        if matrix[i][j]=='*':
            new[i][j]=='*'
        else:
            if matrix[i-1][j]=='*':
                new[i][j]+=1
            if matrix[i+1][j]=='*':
                new[i][j]+=1
            if matrix[i][j-1]=='*':
                new[i][j]+=1
            if matrix[i][j+1]=='*':
                new[i][j]+=1

                
Traceback (most recent call last):
  File "<pyshell#211>", line 2, in <module>
    for j in rang(col):
NameError: name 'rang' is not defined. Did you mean: 'range'?
for i in range(row):
    for j in range(col):
        if matrix[i][j]=='*':
            new[i][j]=='*'
        else:
            if matrix[i-1][j]=='*':
                new[i][j]+=1
            if matrix[i+1][j]=='*':
                new[i][j]+=1
            if matrix[i][j-1]=='*':
                new[i][j]+=1
            if matrix[i][j+1]=='*':
                new[i][j]+=1

                
False
False
False
Traceback (most recent call last):
  File "<pyshell#213>", line 12, in <module>
    if matrix[i][j+1]=='*':
IndexError: list index out of range
for i in range(row):
    for j in range(col):
        if matrix[i][j]=='*':
            new[i][j]=='*'
        else:
            if i!=0:
                if matrix[i-1][j]=='*':
                    new[i][j]+=1
            if i+1!=row:
                if matrix[i+1][j]=='*':
                    new[i][j]+=1
            if j!=0:
                if matrix[i][j-1]=='*':
                    new[i][j]+=1
            if j+1!=col:
                if matrix[i][j+1]=='*':
                    new[i][j]+=1

                    
False
False
False
False
NEW
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    NEW
NameError: name 'NEW' is not defined. Did you mean: 'new'?
new
[[7, 1, 1], [0, 6, 2], [2, 0, 1]]
new = [[0 for i in range(row)] for j in range(col)]
for i in range(row):
    for j in range(col):
        if matrix[i][j]=='*':
            new[i][j]=='*'
        else:
            if i!=0:
                if matrix[i-1][j]=='*':
                    new[i][j]+=1
            if i+1!=row:
                if matrix[i+1][j]=='*':
                    new[i][j]+=1
            if j!=0:
                if matrix[i][j-1]=='*':
                    new[i][j]+=1
            if j+1!=col:
                if matrix[i][j+1]=='*':
                    new[i][j]+=1

                    
False
False
False
False
new
[[2, 0, 0], [0, 3, 1], [2, 0, 1]]
new = [[0 for i in range(row)] for j in range(col)]
for i in range(row):
    for j in range(col):
        if matrix[i][j]=='*':
            new[i][j]='*'
        else:
            if i!=0:
                if matrix[i-1][j]=='*':
                    new[i][j]+=1
            if i+1!=row:
                if matrix[i+1][j]=='*':
                    new[i][j]+=1
            if j!=0:
                if matrix[i][j-1]=='*':
                    new[i][j]+=1
            if j+1!=col:
                if matrix[i][j+1]=='*':
                    new[i][j]+=1

                    
new
[[2, '*', '*'], ['*', 3, 1], [2, '*', 1]]
col, row = map(int, input().split())
matrix=[]
for i in range(row):
    matrix.append(list(input()))
for i in range(row):
    for j in range(col):
        if matrix[i][j]!='*':
            matrix[i][j]=0
            if i!=0:
                if matrix[i-1][j]=='*':
                    new[i][j]+=1
            if i+1!=row:
                if matrix[i+1][j]=='*':
                    new[i][j]+=1
            if j!=0:
                if matrix[i][j-1]=='*':
                    new[i][j]+=1
            if j+1!=col:
                if matrix[i][j+1]=='*':
                    new[i][j]+=1
print(matrix)
SyntaxError: multiple statements found while compiling a single statement
col, row = map(int, input().split())
matrix=[]
for i in range(row):
    matrix.append(list(input()))
for i in range(row):
    for j in range(col):
        if matrix[i][j]!='*':
            matrix[i][j]=0
            if i!=0:
                if matrix[i-1][j]=='*':
                    new[i][j]+=1
            if i+1!=row:
                if matrix[i+1][j]=='*':
                    new[i][j]+=1
            if j!=0:
                if matrix[i][j-1]=='*':
                    new[i][j]+=1
            if j+1!=col:
                if matrix[i][j+1]=='*':
                    new[i][j]+=1
print(matrix)
SyntaxError: multiple statements found while compiling a single statement
col, row = map(int, input().split())
3 3
matrix=[]
for i in range(row):
    matrix.append(list(input()))

    
.**
*..
.*.
for i in range(row):
    for j in range(col):
        if matrix[i][j]!='*':
            matrix[i][j]=0
            if i!=0:
                if matrix[i-1][j]=='*':
                    matrix[i][j]+=1
            if i+1!=row:
                if matrix[i+1][j]=='*':
                    matrix[i][j]+=1
            if j!=0:
                if matrix[i][j-1]=='*':
                    matrix[i][j]+=1
            if j+1!=col:
                if matrix[i][j+1]=='*':
                    matrix[i][j]+=1

                    
print(matrix)
[[2, '*', '*'], ['*', 3, 1], [2, '*', 1]]

col, row = map(int, input().split())
3 3
matrix=[]
for i in range(row):
    matrix.append(list(input()))

    
.**
*..
.*.
for i in range(row):
    for j in range(col):
        if matrix[i][j]!='*':
            matrix[i][j]=0

            
matrix
[[0, '*', '*'], ['*', 0, 0], [0, '*', 0]]
for i in range(1:row-1):
    
SyntaxError: expected ':'
for i in range(row):
    for j in range(col):
        if matrix[i][j]!='*':
            matrix[i][j]=0
            if i!=0:
                if matrix[i-1][j]=='*':
                    matrix[i][j]+=1
                if j!=0:
                    if matrix[i-1][j-1]=='*':
                        matrix[i][j]+=1
                if j+1!=col:
                    if matrix[i-1][j+1]=='*':
                        matrix[i][j]+=1
            if i+1!=row:
                if matrix[i+1][j]=='*':
                    matrix[i][j]+=1
                if j!=0:
                    if matrix[i+1][j-1]=='*':
                        matrix[i][j]+=1
                if j+1!=col:
                    if matrix[i+1][j+1]=='*':
                        matrix[i][j]+=1
            if j!=0:
                if matrix[i][j-1]=='*':
                    matrix[i][j]+=1
            if j+1!=col:
                if matrix[i][j+1]=='*':
                    matrix[i][j]+=1

                    
matrix
[[2, '*', '*'], ['*', 4, 3], [2, '*', 1]]
col, row = map(int, input().split())
3 3
matrix=[]
for i in range(row):
    matrix.append(list(input()))

    
.**
*..
.*.
for i in range(row):
    for j in range(col):
        if matrix[i][j]!='*':
            matrix[i][j]=0
            for x in range(i-1,i+2):
                if x!=-1 and x!=row:
                    for y in range(j-1,j+2):
                        if y!=-1 and y!=col:
                            if matrix[x][y]=='*':
                            matrix[i][j]+=1
                            
SyntaxError: expected an indented block after 'if' statement on line 9
for i in range(row):
    for j in range(col):
        if matrix[i][j]!='*':
            matrix[i][j]=0
            for x in range(i-1,i+2):
                if x!=-1 and x!=row:
                    for y in range(j-1,j+2):
                        if y!=-1 and y!=col:
                            if matrix[x][y]=='*':
                                matrix[i][j]+=1

                                
matrix
[[2, '*', '*'], ['*', 4, 3], [2, '*', 1]]
print(matrix)
[[2, '*', '*'], ['*', 4, 3], [2, '*', 1]]

col, row = map(int, input().split())
3 3
col, row = map(int, input().split())
5 5
matrix=[]
for i in range(row):
    matrix.append(list(input()))

    
..*..
...*.
.*...
.***.
*.*..
for i in range(row):
    for j in range(col):
        if matrix[i][j]!='*':
            matrix[i][j]=0
            for x in range(i-1,i+2):
                if x!=-1 and x!=row:
                    for y in range(j-1,j+2):
                        if y!=-1 and y!=col:
                            if matrix[x][y]=='*':
                                matrix[i][j]+=1

                                
matrix
[[0, 1, '*', 2, 1], [1, 2, 3, '*', 1], [2, '*', 5, 3, 2], [3, '*', '*', '*', 1], ['*', 4, '*', 3, 1]]

========================== RESTART: E:/Python/dkrl.py ==========================
3 3
.**
*..
.*.
[[2, '*', '*'], ['*', 4, 3], [2, '*', 1]]

========================== RESTART: E:/Python/dkrl.py ==========================
3 3
.**
*..
.*.
2
*
*

*
4
3

2
*
1


========================== RESTART: E:/Python/dkrl.py ==========================
3 3
.**
*..
.*.
2**
*43
2*1
col, row = map(int, input().split())
matrix=[]
for i in range(row):
    matrix.append(list(input()))
for i in range(row):
    for j in range(col):
        if matrix[i][j]!='*':
            matrix[i][j]=0
            for x in range(i-1,i+2):
                if x!=-1 and x!=row:
                    for y in range(j-1,j+2):
                        if y!=-1 and y!=col:
                            if matrix[x][y]=='*':
                                matrix[i][j]+=1
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end='')
    print()
