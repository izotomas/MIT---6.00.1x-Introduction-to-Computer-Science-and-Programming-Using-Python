'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
For problems such as these, do not include raw_input statements or define the
variable s in any way. Our automated testing will provide a value of s for you
- so the code you submit in the following box should assume s is already
defined. If you are confused by this instruction, please review L4 Problems 10
and 11 before you begin this problem set.
'''
s = 'azcbobobegghakl'
n = 0
ans = 0
for i in s[0:len(s)-2]:
    if s[n:n+3] == 'bob':
        ans = ans + 1
    n=n+1
print 'Number of times bob occurs is:', ans
