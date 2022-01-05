Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(1,2,3)
1 2 3
print('Hello', 'Python')
Hello Python
print(1,2,3, sep=',')
1,2,3
print('Hello', 'Python', sep='')
HelloPython
print(1920,1080, sep='x')
1920x1080
print(1,2,3, sep='\n')
1
2
3
print('1\n2\n3')
1
2
3
print(1, end='')
1
print(1, end=''); print(2, end=''); print(3)
123

# 연습문제
year=2000; month=10; day=27; hour=11; minute=43; second=59
print(year, month, day, sep='/', end=' '); print(hour, minute, second, sep=':')
2000/10/27 11:43:59

# 심사문제
year, month, day, hour, minute, second = input().split()
1999 12 31 10 37 21
print(year, month, day, sep='-', end='T'); print(hour, minute, second, sep=':')
1999-12-31T10:37:21
