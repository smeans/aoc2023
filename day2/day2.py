import sys
import re

raw = None
with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
    raw = f.read()

ga = raw.splitlines()

samples = {}

for game in ga:
    game_tag, data = game.split(': ')
    game_id = int(game_tag.split(' ')[1])
    samples[game_id] = [
        {v.split(' ')[1]: int(v.split(' ')[0]) for v in gd.split(', ')} for gd in data.split('; ')
    ]

bag ={
        'red': 12,
         'green': 13,
         'blue': 14
}

def is_possible(bag, sa):
    for s in sa:
        for k in s:
            if s[k] > bag[k]:
                return False
    
    return True

sum = 0
for game_id in samples:
    if is_possible(bag, samples[game_id]):
        sum += game_id

print(f'samples: {samples}')
print(f'game_id sum: {sum}')