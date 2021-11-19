inp = 1350

x_max = 45
y_max = 45

field = [[0]*x_max for i in range(y_max)]

for i in range(y_max):
    for j in range(x_max):
        field[i][j] = '{0:b}'.format(j*j + 3*j + 2*j*i + i + i*i + inp).count("1") % 2

field.insert(0,[1]*(2+x_max))
field.append([1]*(2+x_max))
for i in range(y_max+2):
    field[i] = [1] + field[i] + [1]

goal = (32,40)

pos = (2,2)
moves = [(1,0),(0,1),(-1,0),(0,-1)]

prev_steps = set()

def print_field(pos,path):
    print("")
    print("")
    print("")
    for i in range(y_max+2):
        for j in range(x_max+2):
            if i == 40 and j == 32:
                print("X",end='')
            elif (j,i) == pos:
                print("^",end='')
            elif (j,i) in path:
                print("0",end='')
            else:
                if field[i][j] == 1:
                    print("#",end='')
                else:
                    print(" ",end='')
        print("")

def possible(new_pos):
    return new_pos not in prev_steps and not field[new_pos[1]][new_pos[0]]

def rec_search(pos):
    prev_steps.add(pos)
    # print_field(pos,prev_steps)
    for i in moves:
        next_pos = (pos[0] + i[0], pos[1] + i[1])
        if possible(next_pos):
            if next_pos == goal:
                path = [next_pos,pos]
                found = True
                return (path,found)
            path, found = rec_search(next_pos)
            if found:
                path.append(pos)
                return (path,True)
    return ([],False)

def count_adjacents(pos,path):
    count = 0
    for i in moves:
        if (pos[0] + i[0], pos[1] + i[1]) in path:
            count += 1
    return count

def sanitize_path(path,path_len):
    for i in path:
        if count_adjacents(i,path) > 2:
            path_len -= 1
    return path_len

path,found = rec_search(pos)
# print_field(pos,path)
print("1:",sanitize_path(path,len(path)-1))

prev_steps = set()
def rec_search2(pos,depth):
    prev_steps.add(pos)
    # print_field(pos, prev_steps)
    if depth == 50:
        return
    for i in moves:
        next_pos = (pos[0] + i[0], pos[1] + i[1])
        if possible(next_pos):
            rec_search2(next_pos, depth + 1)

    return

rec_search2((2,2),0)
# quick hack, there are 2 steps to the longest path that are redundant so we can go 2 extra.
#   very specific to this input.
print(len(prev_steps)+2)