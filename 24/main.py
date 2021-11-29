import itertools

f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

# pois is a dict with the position of all the points of interest
points = 8
pois = dict()
pois_list = [str(i) for i in range(points)]


for i in range(len(dat)):
    for j in range(len(dat[i])):
        if dat[i][j] in pois_list:
            pois[dat[i][j]] = (j,i)

# printing the field with the visited nodes marked for debugging
def print_field(cur, visited=set()):
    for i in range(len(dat)):
        for j in range(len(dat[i])):
            if (j,i) == cur:
                print("^",end='')
            elif (j, i) in visited:
                print("*",end='')

            else:
                print(dat[i][j],end='')
        print("")

# do a dfs on all pois to get distance to all other pois
def dfs(poi):

    dists = [9999 for i in range(points)]
    dists[int(poi)] = 0
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    queue = [(pois[poi][0], pois[poi][1], 0)]
    visited = set()

    while 9999 in dists:
        cur_pos = queue.pop(0)
        cur_x = cur_pos[0]
        cur_y = cur_pos[1]
        dist = cur_pos[2]


        for i in dirs:
            if dat[cur_y + i[1]][cur_x + i[0]] == "." and (cur_x + i[0], cur_y + i[1]) not in visited:
                queue.append((cur_x + i[0],cur_y + i[1],dist + 1))
                visited.add((cur_x + i[0], cur_y + i[1]))

            if dat[cur_y + i[1]][cur_x + i[0]] in pois_list :
                queue.append((cur_x + i[0],cur_y + i[1],dist + 1))
                if dist + 1 < dists[int(dat[cur_y + i[1]][cur_x + i[0]])]:
                    dists[int(dat[cur_y + i[1]][cur_x + i[0]])] = dist + 1

        #print_field((cur_x,cur_y),visited)
    return dists

# matrix is the distance from->to such that matrix[a][b] gives the distance from a -> b
matrix = []
for i in range(points):
    matrix.append(dfs(str(i)))

# create all permutations of points 1->7, then starting at zero, add up
#   the distance that permutation's path defines and find the min
l = [i for i in range(1,points)]
t = list(itertools.permutations(l))
min = 9999999999
path = []
for i in t:
    cur = 0
    dist = 0
    for j in i:
        dist += matrix[cur][j]
        cur = j
    if dist < min:
        min = dist
        path = i

print("1:",min) #2582 is too high

# part 2 is the same but we have to add point 0 onto the end of each permutation

for i in range(len(t)):
    t[i] = list(t[i]) + [0]

min = 9999999999
path = []
for i in t:
    cur = 0
    dist = 0
    for j in i:
        dist += matrix[cur][j]
        cur = j
    if dist < min:
        min = dist
        path = i

print("2:",min)