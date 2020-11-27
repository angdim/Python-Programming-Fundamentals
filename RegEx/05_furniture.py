import re
template = r'(^>>)(?P<furniture>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)($|\s)'
furniture = []
line = input()
cost = 0
while not line == 'Purchase':
    info = re.match(template, line)
    if info:
        obj = info.groupdict()
        furniture.append(obj['furniture'])
        cost += float(obj['price']) * float(obj['quantity'])
    line = input()
print('Bought furniture:')
for f in furniture:
    print(f)
print(f'Total money spend: {cost:.2f}')
