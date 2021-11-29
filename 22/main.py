f = open("input.txt")

class Node:
    def __init__(self,line):
        l = line.split()
        self.x = int(l[0].split("-")[1][1:])
        self.y = int(l[0].split("-")[-1][1:])

        self.size = int(l[1].replace("T",""))
        self.used = int(l[2].replace("T",""))
        self.avail = int(l[3].replace("T",""))
        self.use_percent = int(l[4].replace("%",""))

    def is_empty(self):
        return self.used == 0

    def __str__(self):
        return str(self.used) + "/" + str(self.avail)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def are_connected(self,other):
        if self == other:
            return False
        return self.used != 0 and self.used < other.avail

dat = [s.strip() for s in f.readlines()]

data = dict()

max_x = 0
max_y = 0
for i in dat:
    if i.startswith("/"):
        n = Node(i)
        data[(n.x,n.y)] = n
        if n.x > max_x:
            max_x = n.x
        if n.y > max_y:
            max_y = n.y

count = 0
for i in list(data.values()):
    for j in list(data.values()):
        if i.are_connected(j):
            count += 1
print("1:",count)

# for this part, you're best bet is to just calculate it by hand. the open spot is at (35,24). it takes 71 steps to
# move the open node to the node just to the left (-1,0) of the important node. from there, it's one step to move the
# important node into that open spot and then 5 steps to move the important node 1 closer to (0,0).
# final count is (71 + 1 + 36*5) = 252 steps

# this is how I found the open node
# adjs = [(1,0),(-1,0),(0,1),(0,-1)]
# for j in range(max_y+1):
#     for i in range(max_x+1):
#         for k in adjs:
#             if (i+k[0],j+k[1]) in data:
#                     if data[(i,j)].are_connected(data[(i+k[0],j+k[1])]):
#                          print("possible move:(" + str(i) + "," + str(j) + ") and (" + str(i+k[0]) + "," + str(j+k[1]) + ")")

# too high 255
print("2:",252)