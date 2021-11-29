import re

f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

count = 0
for i in dat:
    s = re.split('[\[\]]',i)
    possible = False
    # check the even strings (outside of brackets)
    for j in range(0,len(s),2):
        for k in range(len(s[j])-3):
            if s[j][k:k+2] == ''.join(reversed(s[j][k+2:k+4])) and s[j][k] != s[j][k+1]:
                possible = True
                break
        if possible:
            break

    # check the odd strings (inside brackets)
    for j in range(1,len(s),2):
        for k in range(len(s[j]) - 3):
            if s[j][k:k+2] == ''.join(reversed(s[j][k+2:k+4])) and s[j][k] != s[j][k+1]:
                possible = False
                break

    if possible:
        count += 1

print("1: " + str(count))

count2 = 0
for i in dat:
    s = re.split('[\[\]]',i)
    char_a = ''
    char_b = ''
    possible = False
    for j in range(0,len(s),2):
        for k in range(len(s[j])-2):
            if s[j][k] == s[j][k+2] and s[j][k] != s[j][k+1]:
                char_a += s[j][k]
                char_b += s[j][k+1]

    possibles = []
    for j in range(len(char_a)):
        possibles.append(char_b[j]+char_a[j]+char_b[j])

    for j in range(1,len(s),2):
        for k in range(len(s[j])-2):
            if s[j][k:k+3] in possibles:
                possible = True
                count2 += 1
                break
        if possible:
            break

print("2: " + str(count2))