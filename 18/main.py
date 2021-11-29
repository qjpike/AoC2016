f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

width = len(dat)
field = [dat[0]]
traps = ['^^.', '.^^', '^..', '..^']

def get_tile(rang, test):
    val = ''
    for i in rang:
        if 0 <= i < width:
            val += test[rang.index(i)]
        else:
            val += '.'

    if val in traps:
        return '^'
    else:
        return '.'


rows = 3
row = dat[0]
for i in range(rows):
    next_row = ''
    for j in range(len(row)):
        next_row += get_tile([i-1,i,i+1], row[i-1:i+2:1])