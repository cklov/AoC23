with open("data/3.txt") as f:
    lines = f.readlines()

schem = []
for l in lines:
    schem.append(l.strip("\n"))
p1 = 0
p2 = 0
num = ""
gearcheck = []
y = len(schem)
x = len(schem[0])
nums = []
chars = []
for j in range(y):
    for i in range(x):
        if schem[j][i].isdigit():
            num += schem[j][i]
        elif not schem[j][i] == "." and not schem[j][i].isdigit():
            chars.append((schem[j][i], j, i))
        if len(num) > 0 and any([not schem[j][i].isdigit(),  i == (x - 1)]):
            if schem[j][i].isdigit():
                xend = i
            else:
                xend = i - 1
            nums.append((int(num), j, (max(0, i-len(num)), xend)))
            num = ""
for char in chars:    
    for num in nums:
        if max(0, char[1] - 1) <= num[1] <= min(y, char[1] + 1):
            if max(0, num[2][0] - 1) <= char[2] <= min(x, num[2][1] + 1):
                p1 += num[0]
                if char[0] == "*":
                    gearcheck.append(num[0])
    if len(gearcheck) == 2:
        p2 += gearcheck[0] * gearcheck[1]
    gearcheck = []
print(p1)
print(p2)
