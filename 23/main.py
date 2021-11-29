f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

for i in range(len(dat)):
    dat[i] = dat[i].split()

reg_names = ["a","b","c","d"]
regs = [0,0,0,0]

def get_op(op):
    if op in reg_names:
        return regs[reg_names.index(op)]
    else:
        return int(op)

singles = ["dec", "inc", "tgl"]
doubles = ["cpy", "jnz"]
ptr = 0
regs[0] = 12 # for part 1, change this to 7. Part 2 to 12
while ptr < len(dat):
    if dat[ptr][0] == "cpy":
        op1 = get_op(dat[ptr][1])
        op2 = reg_names.index(dat[ptr][2])
        regs[op2] = op1
        ptr += 1
    elif dat[ptr][0] == "jnz":
        if get_op(dat[ptr][1]) == 0:
            ptr += 1
        else:
            ptr += get_op(dat[ptr][2])
    elif dat[ptr][0] == "dec":
        regs[reg_names.index(dat[ptr][1])] -= 1
        ptr += 1
    elif dat[ptr][0] == "inc":
        regs[reg_names.index(dat[ptr][1])] += 1
        ptr += 1
    elif dat[ptr][0] == "tgl":
        op1 = get_op(dat[ptr][1])
        if len(dat) > ptr + op1 >= 0:
            if dat[ptr + op1][0] in singles:
                if dat[ptr+op1][0] == "inc":
                    dat[ptr+op1][0] = "dec"
                else:
                    dat[ptr+op1][0] = "inc"
            elif dat[ptr+op1][0] == "jnz":
                dat[ptr + op1][0] = "cpy"
            elif dat[ptr+op1][0] == "cpy":
                dat[ptr + op1][0] = "jnz"
        ptr += 1
    else:
        print("Invalid Op Code", dat[ptr][0])

print(regs[0])

# part 2 runs very slowly. running using pypy gives you a decent runtime of a few minutes.
# to optimize, you can change the input and add a multiply operator but I didn't do that.
