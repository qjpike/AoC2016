salt = 'ahsbgdzn'

import hashlib as hl

# make a file that has all of the hashes only used in part 2
# f = open("hashes.txt",mode='w')
# for i in range(30000):
#     res = salt + str(i)
#     for j in range(2017):
#         res = hl.md5(res.encode()).hexdigest()
#     f.write(res)
#     f.write("\n")
#
# f.close()

def check_for_trips(str):
    for i in range(len(str)-2):
        if str[i] == str[i+1] and str[i] == str[i+2]:
            return str[i:i+3]
    return False

f = open("hashes.txt")
dat = [i.strip() for i in f.readlines()]

#part 1
valids = set()

threes = [hex(i)[2]*3 for i in range(16)]
fives = [hex(i)[2]*5 for i in range(16)]

threes_dict = dict()
fives_dict = dict()

for i in threes:
    threes_dict[i] = []

for i in fives:
    fives_dict[i] = []

for i in range(50000):
    res = hl.md5((salt+str(i)).encode()).hexdigest()
    t = check_for_trips(res)
    if t:
        threes_dict[t].append(i)

    for j in fives:
        if j in res:
            fives_dict[j].append(i)


for i in range(len(threes)):
    trip = threes_dict[threes[i]]
    quint = fives_dict[fives[i]]

    for j in trip:
        for k in quint:
            if k > j and k <= j+1000:
                valids.add(j)

results = list(valids)
results.sort()

print("1:",results[63])



valids = set()

threes = [hex(i)[2]*3 for i in range(16)]
fives = [hex(i)[2]*5 for i in range(16)]

threes_dict = dict()
fives_dict = dict()

for i in threes:
    threes_dict[i] = []

for i in fives:
    fives_dict[i] = []


for i in dat:
    t = check_for_trips(i)
    if t:
        threes_dict[t].append(dat.index(i))

    for j in fives:
        if j in i:
            fives_dict[j].append(dat.index(i))


for i in range(len(threes)):
    trip = threes_dict[threes[i]]
    quint = fives_dict[fives[i]]

    for j in trip:
        for k in quint:
            if k > j and k <= j+1000:
                valids.add(j)

results = list(valids)
results.sort()

print("2:",results[63])