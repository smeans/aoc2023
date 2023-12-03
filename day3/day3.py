import sys
import re

raw = None
with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
    raw = f.read()

ad = raw.splitlines()
pl = '.' * (len(ad[0]) + 2)
data = [pl, *['.' + row + '.' for row in ad], pl]
print(data)

def checkSpan(row, s):
    s = re.sub(f'[\d\.]+', '', data[row][s[0]-1:s[1]+1])
    return bool(len(s))

def processRow(row):
    sum = 0
    
    rs = data[row]
    for m in re.finditer(r'\d+', data[row]):
        s = m.span(0)
        v = int(m.group())

        if rs[s[0]-1] != '.' or rs[s[1]] != '.':
            sum += v
        elif checkSpan(row-1, s) or checkSpan(row+1, s):
            sum += v
        else:
            print(f'rejecting {v}: row: {row} span: {s}')
    return sum

total = 0
for row in range(1, len(data)):
    total += processRow(row)

print(f'total: {total}')