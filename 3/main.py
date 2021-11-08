f = open("input.txt")


def det_sides(a,b,c):
    if a+b > c:
        return 1
    return 0

count = 0
for i in f.readlines():
    a,b,c = i.split()
    s_count = 0
    s_count += det_sides(int(a),int(b),int(c))
    s_count += det_sides(int(b),int(c),int(a))
    s_count += det_sides(int(c),int(a),int(b))
    if s_count == 3:
        count += 1

print("1: " + str(count))

f.close()
f = open("input.txt")
dat = f.read().split()


count = 0
for i in range(0,len(dat),9):
    for j in range(3):
        a,b,c = (int(dat[i+j]),int(dat[i+j+3]),int(dat[i+j+6]))
        s_count = 0
        s_count += det_sides(int(a),int(b),int(c))
        s_count += det_sides(int(b),int(c),int(a))
        s_count += det_sides(int(c),int(a),int(b))
        if s_count == 3:
            count += 1

print("2: " + str(count))