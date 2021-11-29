f = open("input.txt")
dat = [i for i in f.readlines()]

field = []
new = []
for i in range(6):
    for j in range(50):
        new.append(0)
    field.append(new)
    new = []

for i in dat:
    if i.startswith("rect"):
        size = i.split()[1]
        x = int(size.split("x")[0])
        y = int(size.split("x")[1])
        for j in range(y):
            field[j][:x] = [1]*x

    elif i.startswith("rotate row"):
        row = int(i.split("=")[1].split()[0])
        amt = int(i.split()[-1])
        field[row] = field[row][-amt:] + field[row][:-amt]
    elif i.startswith("rotate column"):
        # transpose field, rotate corresponding "column", transpose again
        col = int(i.split("=")[1].split()[0])
        amt = int(i.split()[-1])
        field = [[row[i] for row in field] for i in range(len(field[0]))]
        field[col] = field[col][-amt:] + field[col][:-amt]
        field = [[row[i] for row in field] for i in range(len(field[0]))]

count = 0
for i in field:
    for j in i:
        count += j

print("1: " + str(count))

for i in field:
    for k in range(6):
        for j in i:
            if j == 0:
                print("     ",end="")
            else:
                print("#####",end="")
        print("")
    print("")

# probably need to zoom out after the print, but answer is "AFBUPZBJPS"

