import hashlib

inp = 'reyedfim'

res = ''
res2 = ['','','','','','','','']
i = 0
res2_c = 0

while len(res) < 8 or res2_c < 8:
    i += 1
    st = inp + str(i)
    t = hashlib.md5(st.encode())
    r = t.hexdigest()
    if r[:5] == '00000':
        if len(res) < 8:
            res += r[5]
        if ord(r[5]) >= ord('0') and ord(r[5]) <= ord('7') and res2[int(r[5])] == '':
            print("Res2: " + r[5] + ":" + r[6])
            res2[int(r[5])] = r[6]
            res2_c += 1



print("1: " + res)
print("2: " + ''.join(res2))

