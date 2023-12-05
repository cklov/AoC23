with open("data/4.txt") as f:
    lines = f.readlines()
p1 = 0
p2 = 0
woncards = {c: 1 for c in range(0, len(lines))}
for i, line in enumerate(lines):
    _, card = line.strip("\n").split(": ")
    win, nums = card.split(" | ")
    win = win.split()
    nums = nums.split()
    score = -1
    p2 += woncards[i]
    for num in nums:
        if num in win:
            score += 1
            woncards[i + score + 1] += woncards[i]
    if score > -1:
        p1 += 2 ** score
print(p1)
print(p2)
