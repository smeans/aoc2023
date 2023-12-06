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
        rmt = (mt[1], mt[0])
    elif not line:
        mt = None
    else:
        if mt not in md:
            md[mt] = []
            md[rmt] = []
        
        nl = parseNums(line)
        md[mt].append(nl)
        md[rmt].append([nl[1], nl[0], nl[2]])

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

def valid_seed(sn):
    for i in range(0,len(seeds), 2):
        if sn >= seeds[i] and sn < seeds[i] + seeds[i+1]:
            return True
        
    return False

la = md[('location', 'humidity')]

la = sorted(la, key=lambda r: r[0])

ln = 0
while True:
    sn = map('location', 'seed', ln)
    
    if valid_seed(sn):
        print(f'location {ln} seed {sn}')
        break

    ln += 1