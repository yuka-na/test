"""
このファイルに解答コードを書いてください
"""
import os
import numpy as np
import re
with open('sample2.txt') as f:
    l_strip = [s.strip() for s in f.readlines()]
    dic = l_strip.copy()
num = []
str = []
for i,dic in enumerate(dic):
    num.append(re.sub("\\D", "", dic))
    str.append(re.findall(':(.*)',dic))
del str[-1]
num = [int(i) for i in num]
k = num[-1]
judge = 0
renum = []
restr = []
for i,number in enumerate(num):
    if(number == k):
        break
    else:
        if(k % number == 0):
            restr.append(str[i])
            renum.append(number)
            judge = 1
        else:
            continue

sorted_idx = np.argsort(renum)
sorted_renum = np.sort(renum)
sorted_restr = []
for i in sorted_idx:
    sorted_restr.append(restr[i])
if judge == 0:
    print(k)
else:
    print(sorted_restr)

f.close()
