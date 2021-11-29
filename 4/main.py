f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

def get_chksum(inp):
    d = dict()
    for i in inp:
        for j in i:
            if j not in d:
                d[j] = 1
            else:
                d[j] += 1

    outp = ''
    while len(outp) < 5:
        max = 0
        t_outp = []
        for z in list(d.keys()):
            if d[z] > max:
                t_outp = [z]
                max = d[z]
            elif d[z] == max:
                t_outp.append(z)

        for z in t_outp:
            d.__delitem__(z)

        t_outp.sort()
        outp += ''.join(t_outp)

    return outp[:5]

count = 0
valid = []
for i in dat:
    inp = i.split("-")
    sect = int(inp[-1].split("[")[0])
    chksum = inp[-1].split("[")[1][:5]
    inp_chksum = get_chksum(inp[:-1])
    if inp_chksum == chksum:
        count += sect
        valid.append(i)

print("1: " + str(count))

def cypher(inp, sect):
    outp = ''
    for i in inp:
        for j in i:
            ordv = ord(j) - ord("a")
            ordv = (ordv + sect) % 26 + ord("a")
            outp += chr(ordv)
        outp += " "

    return outp

sector_name = 'northpole object storage ' # needs the extra space because of outp += ' ' in cypher()
sector = -1
for i in valid:
    inp = i.split("-")
    sect = int(inp[-1].split("[")[0])
    if cypher(inp[:-1],sect) == sector_name:
        sector = sect

print("2: " + str(sector))




