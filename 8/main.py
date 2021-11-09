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
        field[row] = field[row][amt:] + field[row][:amt]
    elif i.startswith("rotate column"):
        col = int(i.split("=")[1].split()[0])
        amt = int(i.split()[-1])
        print("rotate col " + str(col) + " " + str(amt))