import re
participants = input().split(', ')
line = input()
racers = {name: 0 for name in participants}
name_ptn = r'[A-Za-z]'
distance_ptn = r'[\d]'
while not line == 'end of race':
    racer = ''.join(re.findall(name_ptn, line))
    if racer in racers:
        distance = sum([int(d) for d in re.findall(distance_ptn, line)])
        racers[racer] += distance
    line = input()
winners = sorted(racers.items(), key=lambda x: -x[1])
print(f'1st place: {winners[0][0]}')
print(f'2nd place: {winners[1][0]}')
print(f'3rd place: {winners[2][0]}')
