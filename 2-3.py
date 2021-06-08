# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

answer = list(map(int, input().split()))
point = list(map(int, input().split()))
n = input()
temp = {}
Ltemp = []

for x in range(len(answer)):
    temp[x] = 0
for i in range(int(n)):
    space = list(map(int, input().split()))
    for j in range(len(space)):
        if space[j] == answer[j]:
            temp[j] += 1
Ltemp = list(temp.keys())
for v in range(len(answer)):
    if temp[v] == min(temp.values()):
        print(Ltemp[v]+1," ", end='')
