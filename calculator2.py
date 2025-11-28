import re

a, operator, c = re.split('([+*-/])', input())  # splits input like '3+4' into ['3', '+', '4']
a = int(a)
c = int(c)

if operator == '+':
    print(a + c)
if operator == '-':
    print(a - c)
if operator == '*':
    print(a * c)
if operator =="/":
    print(a//c)