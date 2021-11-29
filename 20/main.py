f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

blocks = []
for i in dat:
    inp = i.split("-")

    blocks.append((int(inp[0]),int(inp[1])))

blocks.sort()

next = 1
for i in blocks:
    if i[0] > next:
        break
    elif i[1] > next:
        next = i[1] + 1

print("1:",next)

max = 4294967295
blocks.append((max+1,max+2))
next = 1
count = 0
for i in blocks:
    if i[0] > next:
        count += i[0] - next
    if i[1] > next:
        next = i[1] + 1

print("2:",count)