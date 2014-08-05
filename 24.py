#/usr/bin/env python
#coding:utf-8

from itertools import permutations

number = [["100.0","4.0","4.0","2.0"]]
ops = ["+","-","*","/"]

def get24(res_1):
    if len(res_1[0]) == 1:
        return res_1
    else:
        result = []
        for j in res_1:
            per_num = list(permutations(j,2))
            for i in per_num:
                for op in ops:
                    tmp = j[:]
                    tmp.remove(i[0])
                    tmp.remove(i[1])
                    tmp.append("(" + i[0] + op + i[1] + ")")
                    result.append(tmp)
    return get24(result)

res_1 = get24(number)
for i in res_1:
    try:
        if eval(i[0]) == 24.0:
            print i[0]
    except:
        pass
