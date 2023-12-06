with open("data/5.txt") as f:
    lines = f.read().split("\n\n")

seeds = [int(x) for x in lines[0].strip("seeds: ").split()]
maps = []
for section in lines[1:]:
    mapsection = []
    for line in section.split("\n")[1:]:
        mapsection.append([int(x) for x in line.split()])
    maps.append(mapsection)
locp1 = []
for seed in seeds:
    temp = seed
    for map in maps:
        for p in map:
            d, s, r = p
            if s <= temp < s + r:
                temp = d + temp - s
                break
    locp1.append(temp)
p1 = min(locp1)
print(p1)
i = 0
input = [(s, s + e) for s, e in list(zip(seeds[::2], seeds[1::2]))]
for map in maps:
    output = []
    while len(input) > 0:
        s, e = input.pop()
        for p in map:
            a, b, c = p
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                output.append((os - b + a, oe - b + a))
                if os > s:
                    input.append((s, os))
                if e > oe:
                    input.append((oe, e))
                break
        else:
            output.append((s, e))
    input = output
p2 = min(input)[0]
print(p2)                

