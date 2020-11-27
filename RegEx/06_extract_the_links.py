import re
text = ''
while True:
    line = input()
    if line:
        text += ' ' + line
    else:
        break
template = r'www\.[A-Za-z0-9-]+(\.[a-z]+)+'
sites = re.finditer(template, text)
for site in sites:
    print(site.group())
