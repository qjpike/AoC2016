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

ptr = 0
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
            ptr += int(dat[ptr][2])
    elif dat[ptr][0] == "dec":
        regs[reg_names.index(dat[ptr][1])] -= 1
        ptr += 1
    elif dat[ptr][0] == "inc":
        regs[reg_names.index(dat[ptr][1])] += 1
        ptr += 1
    else:
        print("Invalid Op Code", dat[ptr][0])

print(regs[0])

regs = [0,0,1,0]

ptr = 0
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
            ptr += int(dat[ptr][2])
    elif dat[ptr][0] == "dec":
        regs[reg_names.index(dat[ptr][1])] -= 1
        ptr += 1
    elif dat[ptr][0] == "inc":
        regs[reg_names.index(dat[ptr][1])] += 1
        ptr += 1
    else:
        print("Invalid Op Code", dat[ptr][0])

print(regs[0])