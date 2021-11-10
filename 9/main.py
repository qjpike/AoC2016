import re

f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

uncomps = []
for i in dat:
    outp = ''
    s = i
    if "(" not in s:
        uncomps.append(s)
    else:
        outp += s[:s.index("(")]
        ptr = s.index(")")


        print(outp)
        print(s[s.rindex("(")+1:ptr].split("x"))



print(uncomps)