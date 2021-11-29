f = open("input.txt")
dat = [i.split() for i in f.readlines()]

discs = dict()
positions = []
curr_pos = []
for i in dat:
    positions.append(int(i[3]))
    curr_pos.append(int(i[11][:-1]))


hole_pos = [positions[0]-1, positions[1]-2,positions[2]-3,positions[3]-4,positions[4]-5,positions[5]-6]
t = 0
while curr_pos != hole_pos:
    for i in range(len(curr_pos)):
        curr_pos[i] = ( curr_pos[i] + 1 )%positions[i]
    t += 1
print(t)

curr_pos = []
for i in dat:
    curr_pos.append(int(i[11][:-1]))
curr_pos.append(0)
positions.append(11)
hole_pos.append(positions[6]-7)

t = 0
while curr_pos != hole_pos:
    for i in range(len(curr_pos)):
        curr_pos[i] = ( curr_pos[i] + 1 )%positions[i]
    t += 1
print(t)