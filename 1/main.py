f = open("input.txt")
dat = [i.strip() for i in f.read().split(",")]

x = 0
y = 0
orient = 0


for i in dat:
    if i[0] == "L":
        orient -= 1
    if i[0] == "R":
        orient += 1

    orient %= 4

    if orient == 0:
        y += int(i[1:])
    elif orient == 1:
        x += int(i[1:])
    elif orient == 2:
        y -= int(i[1:])
    elif orient == 3:
        x -= int(i[1:])


print("1: " + str(abs(x) + abs(y)))

x = 0
y = 0
orient = 0
past = []
for j in dat:
    if j[0] == "L":
        orient -= 1
    elif j[0] == "R":
        orient += 1

    orient %= 4
    found = False
    if orient == 0:
        for i in range(y + 1,y + int(j[1:]) + 1):
            if (x,i) in past:
                y = i
                print("2: " + str(abs(x) + abs(y)))
                found = True
                break
            else:
                past.append((x,i))
        if not found:
            y += int(j[1:])
    elif orient == 1:
        for i in range(x + 1, x + int(j[1:]) + 1):
            if (i, y) in past:
                x = i
                print("2: " + str(abs(x) + abs(y)))
                found = True
                break
            else:
                past.append((i, y))
        if not found:
            x += int(j[1:])
    elif orient == 2:
        for i in range(y - 1 , y - int(j[1:]) - 1, -1):
            if (x, i) in past:
                y = i
                print("2: " + str(abs(x) + abs(y)))
                found = True
                break
            else:
                past.append((x, i))
        if not found:
            y -= int(j[1:])
    elif orient == 3:
        for i in range(x - 1, x - int(j[1:]) - 1,-1):
            if (i, y) in past:
                x = i
                print("2: " + str(abs(x) + abs(y)))
                found = True
                break
            else:
                past.append((i, y))
        if not found:
            x -= int(j[1:])

    if found:
        break

