import re
line = input()
template = r'(?<=\b_{1})[A-Za-z0-9]+\b'
variables = re.findall(template, line)
print(','.join(variables))
