import sys
import re

raw = None
with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
    raw = f.read()

ad = raw.splitlines()
pl = '.' * (len(ad[0]) + 2)
data = [pl, *['.' + row + '.' for row in ad], pl]
print(data)

def getAdjacentNums(row, i):
    dl = []
    for cr in range(row-1, row+2):
        for m in re.finditer(r'\d+', data[cr]):
            start, end = m.span(0)
            if ((start <= i and end >= i)
                    or start == i+1):
                dl.append(int(m.group()))
    
    return dl

def processRow(row):
    sum = 0
    
    rs = data[row]
    for m in re.finditer(r'\*', data[row]):
        i = m.span(0)[0]

        nl = getAdjacentNums(row, i)

        print(f'gear: row {row}: {nl}')
        if len(nl) == 2:
            sum += nl[0] * nl[1]

    return sum

total = 0
for row in range(1, len(data)):
    total += processRow(row)

print(f'total: {total}')
