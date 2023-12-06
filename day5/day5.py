import sys
import re

raw = None
with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
    raw = f.read()

ad = raw.splitlines()

def parseNums(s):
    return [int(v) for v in s.split(' ')]

seeds = parseNums(ad[0].split(': ')[1])

md = {}

mt = None
for line in ad[2:]:
    if not mt:
        mt = tuple(line.split(' ')[0].split('-to-'))
    elif not line:
        mt = None
    else:
        if mt not in md:
            md[mt] = []
        
        md[mt].append(parseNums(line))

print(seeds)
print(md)

def map_num(nm, sn):
    for row in nm:
        d, s, r = row

        if sn >= s and sn < s + r:
            return d + (sn -s)
        
    return sn

def map(st, dt, sn):
    kl = [k for k in md.keys() if k[0] == st]
    for k in kl:
        dn = map_num(md[k], sn)
        if k[1] == dt:
            return dn

        dn = map(k[1], dt, dn)
        if dn is not None:
            return dn

    return None

s2l = [map('seed', 'location', sn) for sn in seeds]
print(min(s2l))