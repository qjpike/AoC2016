

def scramble(password, dat, flip=False):

    i_str = password

    if flip:
        dat.reverse()

    for i in dat:
        inp = i.split()
        if inp[0] == "swap":
            if inp[1] == "position":
                pos_a = int(inp[2]) if int(inp[2]) < int(inp[5]) else int(inp[5])
                pos_b = int(inp[5]) if int(inp[2]) < int(inp[5]) else int(inp[2])
                new_str = i_str[:pos_a] + i_str[pos_b] + i_str[pos_a + 1:pos_b] + i_str[pos_a] + i_str[pos_b+1:]
            elif inp[1] == "letter":
                pos_a = i_str.find(inp[2]) if i_str.find(inp[2]) < i_str.find(inp[5]) else i_str.find(inp[5])
                pos_b = i_str.find(inp[5]) if i_str.find(inp[2]) < i_str.find(inp[5]) else i_str.find(inp[2])
                new_str = i_str[:pos_a] + i_str[pos_b] + i_str[pos_a + 1:pos_b] + i_str[pos_a] + i_str[pos_b+1:]
        elif inp[0] == "rotate":
            if inp[1] == "left":
                rot_val = int(inp[2])
                new_str = i_str[rot_val:] + i_str[:rot_val]
            elif inp[1] == "right":
                rot_val = int(inp[2])
                new_str = i_str[-rot_val:] + i_str[:-rot_val]
            elif inp[1] == 'based':
                rot_val = 1 + i_str.find(inp[6])
                if i_str.find(inp[6]) >= 4:
                    rot_val += 1
                rot_val %= len(i_str)
                new_str = i_str[-rot_val:] + i_str[:-rot_val]
        elif inp[0] == "reverse":
            pos_a = int(inp[2]) if int(inp[2]) < int(inp[4]) else int(inp[4])
            pos_b = int(inp[4]) if int(inp[2]) < int(inp[4]) else int(inp[2])
            new_str = i_str[:pos_a] + ''.join(reversed(i_str[pos_a:pos_b+1])) + i_str[pos_b+1:]
        elif inp[0] == "move":
            pos_a = int(inp[2])
            pos_b = int(inp[5])
            str_a = i_str[:pos_a] + i_str[pos_a + 1:]
            new_str = str_a[:pos_b] + i_str[pos_a] + str_a[pos_b:]

        i_str = new_str

    return i_str

import itertools

f = open("input.txt")
dat = [i.strip() for i in f.readlines()]
f.close()

print("1:", scramble("abcdefgh",dat))

scrambled = 'fbgdceah'
for s in itertools.permutations(scrambled):
    if scramble(''.join(s), dat) == scrambled:
        print("2:",''.join(s))
        break

