import sys
import re
import math

raw = None
with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
    raw = f.read()

ad = raw.splitlines()

def parseNums(s):
    return [int(v.strip()) for v in re.split('\s+', s.strip())]

time = parseNums(ad[0].split(": ")[1])
distance = parseNums(ad[1].split(": ")[1])

def num_ways(t, d):
    c = 0

    for i in range(0, t+1):
        if (t-i) * i > d:
            c += 1
    
    return c

tc = [num_ways(time[i], distance[i]) for i in range(len(time))]

print(f'combinations {math.prod(tc)}')