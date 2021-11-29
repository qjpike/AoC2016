import collections
inp = 3014603
elves = collections.deque(range(1,inp+1))

while len(elves) > 1:
    elves.rotate(-1)
    elves.popleft()

print("1:",elves[0]) # 1834903 correct number
# Wrong: 2855755 (too high) 2724607 (too high) 1179701 too low

# VERY WEIRD PATTERN (probably math stuff)
# for the answer you can use the pattern:
# starting at elf count = 4 and (known) prev max winner = 3
# 5 -> 1    increment winner by 1 until the current winner is equal to the prev max winner
# 6 -> 2
# 7 -> 3    Once current winner == prev max winner, increment by 2 until the current winner == elf count
# 8 -> 5
# 9 -> 7
#10 -> 9
#11 ->11    Then make prev max winner equal to this number, and start counting at 1 again
#12 -> 1
#13 -> 2    and so on

# This section prints the pattern for (# of elves: winner)
# for i in range(2,400):
#     elves = collections.deque(range(1,i+1))
#
#     while(len(elves)) > 1:
#         leng = len(elves)
#         elves.rotate(-((leng//2)))
#         elves.popleft()
#         elves.rotate(leng//2)
#         elves.rotate(-1)
#
#     print(i,":",elves[0])

prev_winner = 3
curr_winner = 1
for i in range(4,inp):
    if curr_winner > i:
        prev_winner = curr_winner - 2
        curr_winner = 1
    if curr_winner < prev_winner:
        curr_winner += 1
    else:
        curr_winner += 2

print("2:",curr_winner)