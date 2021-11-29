
f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

res = [dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict()]

for i in dat:
    for j in range(len(i)):
        if i[j] in res[j]:
            res[j][i[j]] += 1
        else:
            res[j][i[j]] = 1

res2 = []
for i in res:
    max = 0
    max_char = ''
    for j in list(i.keys()):
        if i[j] > max:
            max_char = j
            max = i[j]
    res2.append(max_char)

print("1: " + "".join(res2))

res3 = []
for i in res:
    min = 999
    min_char = ''
    for j in list(i.keys()):
        if i[j] < min:
            min_char = j
            min = i[j]
    res3.append(min_char)

print("2: " + "".join(res3))
