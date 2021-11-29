f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

posx = 0
posy = 0
code = []
for i in dat:
    for j in i:
        if j == "R":
            posx += 1
        elif j == "D":
            posy += 1
        elif j == "L":
            posx -= 1
        elif j == "U":
            posy -= 1

        if posx > 1:
            posx = 1
        elif posx < -1:
            posx = -1

        if posy > 1:
            posy = 1
        elif posy < -1:
            posy = -1

    code.append((posx, posy))

poss = [(-1,-1), (0,-1),(1,-1),(-1,0),(0,0),(1,0),(-1,1),(0,1),(1,1)]
butts = [1,2,3,4,5,6,7,8,9]

out = ""
for i in code:
    out += str(butts[poss.index(i)])

print("1: " + out)

posx = 0
posy = 2
code = ''

########
# to determine position/button combinations
# 0 1 2 3 4
#     1		    0
#   2 3 4		1
# 5 6 7 8 9	    2
#   A B C		3
#     D		    4

poss = [(2,0), (1,1), (2,1), (3,1), (0,2), (1,2), (2,2), (3,2), (4,2), (1,3), (2,3), (3,3), (2,4)]
butts = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D']
for i in dat:
    for j in i:
        if j == "R":
            if (posx + 1, posy) in poss:
                posx += 1
        elif j == "D":
            if (posx, posy + 1) in poss:
                posy += 1
        elif j == "L":
            if (posx - 1, posy) in poss:
                posx -= 1
        elif j == "U":
            if (posy - 1, posx) in poss:
                posy -= 1

    code += butts[poss.index((posx,posy))]

print("2: " + code)