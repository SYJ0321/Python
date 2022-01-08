# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

hello = 'Hello, world!'
hello
# 'Hello, world!'

hello = '안녕하세요'
hello
# '안녕하세요'

hello = "Hello, world!"; hello
# 'Hello, world!'
hello = '''Hello, Python!'''; hello
# 'Hello, Python!'
python = """Python Programming"""; python
# 'Python Programming'

# 여러 줄 입력하기
hello = '''Hello, world!
안녕하세요.
Python입니다.'''
print(hello)
# Hello, world!
# 안녕하세요.
# Python입니다.

s = "Python isn't difficult"
s
# "Python isn't difficult"
s = 'He said "Python is easy"'
s
# 'He said "Python is easy"'

'Python isn\'t difficult'
# "Python isn't difficult"

print('Hello\nPython')
# Hello
# Python

# 연습문제
s = '''Python is a programming language that lets you work quickly
and
integrate systems more effectively.'''
print(s)
# Python is a programming language that lets you work quickly
# and
# integrate systems more effectively.

# 심사문제
s = """'Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively."""
print(s)
# 'Python' is a "programming language"
# that lets you work quickly
# and
# integrate systems more effectively.
