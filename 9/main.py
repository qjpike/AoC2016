import re

f = open("input.txt")
dat = f.read().strip()

uncomps = []

len = 0
ptr = 0
while ptr < dat.__len__():
    if dat[ptr] != "(":
        len += 1
    else:
        chrs, times = dat[ptr + 1:dat[ptr + 1:].index(")") + ptr + 1].split("x")
        len += int(chrs) * int(times)
        ptr += int(chrs) + dat[ptr :].index(")")
    ptr += 1

print("1: " + str(len))

weights = [1]*dat.__len__()
len = 0
ptr = 0

#part 2 doesn't work.
while ptr < dat.__len__():
    if dat[ptr] != "(":
        len += weights[ptr]
        ptr += 1
    else:
        chrs, times = dat[ptr + 1:dat[ptr + 1:].index(")") + ptr + 1].split("x")
        ptr += dat[ptr :].index(")") + 1
        for i in range(int(chrs)):
            weights[ptr+i] *= int(times)

print("2: " + str(len))