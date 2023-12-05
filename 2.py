with open("2.txt") as f:
    lines = f.readlines()

possible = {"red": 12, "green": 13, "blue": 14}
p1 = 0
p2 = 0
for i, l in enumerate(lines):
    minkubes = {"red": [], "green": [], "blue": []}
    l = l.split(": ")[1].replace("\n", "").split("; ")
    pos = True
    for draw in l:
        for numclr in draw.split(", "):
            num, clr = numclr.split(" ")
            if int(num) > possible[clr]:
                pos = False
            minkubes[clr].append(int(num))
    if pos:
        p1 += (i + 1)
    p2 += (max(minkubes["red"]) * max(minkubes["green"]) * max(minkubes["blue"]))
print(p1)
print(p2)
