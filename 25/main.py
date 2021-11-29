f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

for i in range(len(dat)):
    dat[i] = dat[i].split()

reg_names = ["a","b","c","d"]


def get_op(op,regs):
    if op in reg_names:
        return regs[reg_names.index(op)]
    else:
        return int(op)

def run_prog(regs):
    singles = ["dec", "inc", "tgl"]
    doubles = ["cpy", "jnz"]
    ptr = 0
    cnt = 0
    out = []
    while ptr < len(dat):
        if dat[ptr][0] == "cpy":
            op1 = get_op(dat[ptr][1],regs)
            op2 = reg_names.index(dat[ptr][2])
            regs[op2] = op1
            ptr += 1
        elif dat[ptr][0] == "jnz":
            if get_op(dat[ptr][1],regs) == 0:
                ptr += 1
            else:
                ptr += get_op(dat[ptr][2],regs)
        elif dat[ptr][0] == "dec":
            regs[reg_names.index(dat[ptr][1])] -= 1
            ptr += 1
        elif dat[ptr][0] == "inc":
            regs[reg_names.index(dat[ptr][1])] += 1
            ptr += 1
        elif dat[ptr][0] == "tgl":
            op1 = get_op(dat[ptr][1],regs)
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
        elif dat[ptr][0] == "out":

            out.append(get_op(dat[ptr][1],regs))
            cnt += 1
            ptr += 1
            if cnt > 11:
                return out
        else:
            print("Invalid Op Code", dat[ptr][0])

# the output repeats itself after 12 characters, so we're only interested in that.
test_val = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
i = 0
while run_prog([i,0,0,0]) != test_val:
    i += 1


print("1:",i)
