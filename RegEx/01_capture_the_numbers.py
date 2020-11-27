import re
lines = ''
while True:
    line = input()
    if line:
        lines += ' ' + line
    else:
        break
template = r'\d+'
numbers = ' '.join(re.findall(template, lines))
print(numbers)
