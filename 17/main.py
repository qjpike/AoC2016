import hashlib as hl

passcode = 'hhhxzeay'

moves = ["U","D","L","R"]
moves_coord = [(0,-1),(0,1),(-1,0),(1,0)]

found = False
# BFS
q = ['']

# returns True if the whole path will stay inside the (0,0), (3,3) square
def possible(path):
    pos = (0,0)
    for i in path:
        next_pos = (pos[0] + moves_coord[moves.index(i)][0], pos[1] + moves_coord[moves.index(i)][1])
        if next_pos[0] > 3 or next_pos [0] < 0 or next_pos[1] > 3 or next_pos[1] < 0:
            return (False, (0,0))
        else:
            pos = next_pos
        if pos == (3,3):
            break
    return (True, pos)

max = 0
while len(q) > 0:
    path = q.pop(0)
    if possible(path):
        res = hl.md5((passcode+path).encode()).hexdigest()[:4]
        for i in range(len(res)):
            if ord("b") <= ord(res[i]) <= ord("f"):
                valid, pos = possible(path + moves[i])
                if pos == (3, 3):
                    if not found:
                        shortest_path = path + moves[i]
                        found = True
                    if len(path) > max:
                        # not sure why it's one less but it holds true for all examples and the formal input.
                        max = len(path) + 1
                        # print(max)
                elif valid:
                    q.append(path+moves[i])

print("Shortest Path:",shortest_path)
print("Longest Path Length:",max)
# 151 is too low