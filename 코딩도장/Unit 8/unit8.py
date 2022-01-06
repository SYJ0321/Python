# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

True; False
# True
# False

3>1
# True
10==10
# True
10!=5
# True

# 문자열 비교
'Python' == 'Python'
# True
'Python' == 'python'
# False

# 객체 비교
1 is 1.0
# False
1 is not 1.0
# True

# 객체의 고유값
id(1)
# 2193238982896
id(1.0)
# 2193243435280

#논리 연산자
True and True; True and False; False and False
# True
# False
# False
True or True; True or False; False or False
# True
# True
# False
not True; not False
# False
# True
not True and False or not False
# True

# 불로 변환하기
bool(1); bool(0)
# True
# False
bool(1.5)
# True
bool('False')
# True

# 단락 평가
True and 'Python'; 'Python' and True; False and 'Python'
# 'Python'
# True
# False
True or 'Python'; 'Python' or True; False or 'Python'
# True
# 'Python'
# 'Python'

# 연습문제
korean = 92; english = 47; mathematics = 86; science = 81
print(korean>=50 and english>50 and mathematics>=50 and science>=50)
# False

# 심사문제
kor, eng, mat, sci = map(int, input().split())
print(kor >= 90 and eng > 80 and mat > 85 and sci >= 80)
# 90 81 86 80
# True
