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

def get_power(sa):
    mins = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for s in sa:
        for k in s:
            if s[k] > mins[k]:
                mins[k] = s[k]
    
    p = 1
    for v in mins.values():
        p *= v

    return p

sum = sum([get_power(s) for s in samples.values()])

print(f'game_id sum: {sum}')