data = '00111101111101000'
length = 272

def create_data(inp,l):
    s = inp
    while len(s) < l:
        a = s
        b = a[::-1]
        b = ''.join([str(abs(int(i)-1)) for i in b])
        s = a + "0" + b
    return s[:length]

def calc_checksum(inp):
    s = inp
    while len(s) % 2 == 0:
        new_s = ''
        for i in range(0,len(s),2):
            if s[i:i+2].count("1") % 2 == 0:
                new_s += "1"
            else:
                new_s += "0"
        s = new_s
    return s

s = create_data(data,length)
print("1:",calc_checksum(s))

length = 35651584
s = create_data(data,length)
print("2:",calc_checksum(s))