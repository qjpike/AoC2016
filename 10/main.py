f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

def give(d, dest, val):
    if dest in d:
        d[dest].append(val)
        d[dest].sort()
    else:
        d[dest] = []
        d[dest].append(val)


robots = dict()
bins = dict()

goal_bot = -1
found = False
inst_queue = [i for i in dat]
i = 0
while len(inst_queue) != 0:
    q = inst_queue.pop(0)
    if q.startswith("value"):
        instr = q.split()
        bot = int(instr[-1])
        val = int(instr[1])
        give(robots, bot, val)

    elif q.startswith("bot"):
        instr = q.split()
        bot = int(instr[1])
        if bot in robots and len(robots[bot]) > 1:
            low_dest = instr[5]
            low = int(instr[6])
            high_dest = instr[-2]
            high = int(instr[-1])
            # print("Robot " + str(bot) + " gives " + str(robots[bot][0]) + " to " + low_dest + " " + str(low) + " and " + str(robots[bot][-1]) + " to " + high_dest + " " + str(high))
            if robots[bot][0] == 17 and robots[bot][-1] == 61:
                print("1: ", bot)

            if low_dest == "bot":
                give(robots, low, robots[bot].pop(0))
            elif low_dest == "output":
                give(bins, low, robots[bot].pop(0))

            if high_dest == "bot":
                give(robots, high, robots[bot].pop(-1))
            elif high_dest == "output":
                give(bins, high, robots[bot].pop(-1))

        else:
            inst_queue.append(q)



print("2: ", bins[0][0]*bins[1][0]*bins[2][0])