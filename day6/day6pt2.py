import sys
import re
import math

raw = None
with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
    raw = f.read()

ad = raw.splitlines()

time = int(re.sub('\s+', '', ad[0].split(": ")[1]))
distance = int(re.sub('\s+', '', ad[1].split(": ")[1]))

print(time, distance)

def time2dist(t):
    return (time-t)*t

t = 0
while t < time and (time-t) * t < distance:
    t += 1

mint = t

t = time
while t > 0 and (time-t) * t < distance:
    t -= 1

maxt = t

print(f'mint {mint} (dist {time2dist(mint)}) maxt {maxt} (distance {time2dist(maxt)})')
print(f'{maxt-mint+1} ways')