Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(100):
    if i%3==0:
        if i%5==0:
            print('FizzBuzz', end='')
        else:
            print('Fizz', end='')
    elif i%5==0:
        if i%3==0:
            continue
        else:
            print('Buzz', end='')
    ele:
        
SyntaxError: invalid syntax
for i in range(100):
    if i%3==0:
        if i%5==0:
            print('FizzBuzz', end='')
        else:
            print('Fizz', end='')
    elif i%5==0:
        if i%3==0:
            continue
        else:
            print('Buzz', end='')
    else:
        print(i, end='')

        
FizzBuzz12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19BuzzFizz2223FizzBuzz26Fizz2829FizzBuzz3132Fizz34BuzzFizz3738FizzBuzz41Fizz4344FizzBuzz4647Fizz49BuzzFizz5253FizzBuzz56Fizz5859FizzBuzz6162Fizz64BuzzFizz6768FizzBuzz71Fizz7374FizzBuzz7677Fizz79BuzzFizz8283FizzBuzz86Fizz8889FizzBuzz9192Fizz94BuzzFizz9798Fizz
for i in range(1,101):
    if i%3==0:
        if i%5==0:
            print('FizzBuzz', end=' ')
        else:
            print('Fizz', end=' ')
    elif i%5==0:
        if i%3==0:
            continue
        else:
            print('Buzz', end=' ')
    else:
        print(i, end=' ')

        
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz 

# 1부터 100까지 출력하기
for i in range(1,101):
    print(i, end=' ')

    
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 

# 3의 배수와 5의 배수 처리
for i in range(1,101):
    if i%3==0:
        print('Fizz', end=' ')
    elif i%5==0:
        print('Buzz', end=' ')
    else:
        print(i, end=' ')

        
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 Fizz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 Fizz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 Fizz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 Fizz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 Fizz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz 

# 3과 5의 공배수 처리
for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz', end=' ')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

        
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz 16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz 31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz 46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz 61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz 76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz 91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

        
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz

# 논리 연산자를 사용하지 않는 방법
for i in range(1,101):
    if i%15==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

        
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz

# 코드 단축하기
for i in range(1,101):
    print('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or i)

    
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz

# 연습문제
for i in range(1,101):
    if i%2==0 or i%11==0:
        print('FizzBuzz')
    elif i%2==0:
        print('Fizz')
    elif i%11==0:
        print('Buzz')
    else:
        print(i)

        
1
FizzBuzz
3
FizzBuzz
5
FizzBuzz
7
FizzBuzz
9
FizzBuzz
FizzBuzz
FizzBuzz
13
FizzBuzz
15
FizzBuzz
17
FizzBuzz
19
FizzBuzz
21
FizzBuzz
23
FizzBuzz
25
FizzBuzz
27
FizzBuzz
29
FizzBuzz
31
FizzBuzz
FizzBuzz
FizzBuzz
35
FizzBuzz
37
FizzBuzz
39
FizzBuzz
41
FizzBuzz
43
FizzBuzz
45
FizzBuzz
47
FizzBuzz
49
FizzBuzz
51
FizzBuzz
53
FizzBuzz
FizzBuzz
FizzBuzz
57
FizzBuzz
59
FizzBuzz
61
FizzBuzz
63
FizzBuzz
65
FizzBuzz
67
FizzBuzz
69
FizzBuzz
71
FizzBuzz
73
FizzBuzz
75
FizzBuzz
FizzBuzz
FizzBuzz
79
FizzBuzz
81
FizzBuzz
83
FizzBuzz
85
FizzBuzz
87
FizzBuzz
89
FizzBuzz
91
FizzBuzz
93
FizzBuzz
95
FizzBuzz
97
FizzBuzz
FizzBuzz
FizzBuzz
for i in range(1,101):
    if i%2==0 and i%11==0:
        print('FizzBuzz')
    elif i%2==0:
        print('Fizz')
    elif i%11==0:
        print('Buzz')
    else:
        print(i)

        
1
Fizz
3
Fizz
5
Fizz
7
Fizz
9
Fizz
Buzz
Fizz
13
Fizz
15
Fizz
17
Fizz
19
Fizz
21
FizzBuzz
23
Fizz
25
Fizz
27
Fizz
29
Fizz
31
Fizz
Buzz
Fizz
35
Fizz
37
Fizz
39
Fizz
41
Fizz
43
FizzBuzz
45
Fizz
47
Fizz
49
Fizz
51
Fizz
53
Fizz
Buzz
Fizz
57
Fizz
59
Fizz
61
Fizz
63
Fizz
65
FizzBuzz
67
Fizz
69
Fizz
71
Fizz
73
Fizz
75
Fizz
Buzz
Fizz
79
Fizz
81
Fizz
83
Fizz
85
Fizz
87
FizzBuzz
89
Fizz
91
Fizz
93
Fizz
95
Fizz
97
Fizz
Buzz
Fizz

# 심사문제
x=int(input())
35
y=int(input())
40
for i in range(x,y):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)

        
FizzBuzz
36
37
38
39
for i in range(x,y+1):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)

        
FizzBuzz
36
37
38
39
Fizz
for i in range(x,y+1):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)

        
FizzBuzz
36
37
38
39
Fizz
x,y=map(int, input().split())

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    x,y=map(int, input().split())
ValueError: not enough values to unpack (expected 2, got 0)
x,y = int(input().split())
35 40
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    x,y = int(input().split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
x,y=map(int, input().split()
        )
35 40
x
35
u
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    u
NameError: name 'u' is not defined
y
40
