with open("1.txt") as f:
    lines = f.readlines()
sum = 0
strint = [str(i) for i in range(1, 10)]
for l in lines:
    l = [n for n in l if n in strint]
    sum += int(l[0] + l[-1])
print(sum)

with open("1.txt") as f:
    lines = f.readlines()
numdict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
sum = 0
for l in lines:
    nl = ""
    digs = []
    for c in l:
        if c in strint:
            digs.append(c)
        else:
            nl += c
            for key, val in numdict.items():
                if nl.endswith(key):
                    digs.append(val)
                    break
    sum += int(digs[0] + digs[-1])
print(sum)