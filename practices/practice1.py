# -*- coding: utf-8 -*-
# practice 1
Max = 299
Min = 0

def reg(num):
    if num > Max:
        return Max
    elif num < Min:
        return Min
    else:
        return num

def solution(input_list):
    output_set = []
    huaxian = []
    for x in input_list:
        if x[0] == "biaozhu":
            output_set.append((x[0], reg(x[1]), reg(x[2]), x[3]))
        else:
            huaxian.append([x[0], reg(x[1]), reg(x[2])])
    huaxian=sorted(huaxian, key=lambda huaxian : huaxian[1])
    for number in range(1, len(huaxian)):
        if huaxian[number][1] > huaxian[number-1][2]:
            output_set.append(tuple(huaxian[number-1]))
        else:
            huaxian[number][1] = huaxian[number-1][1]
            huaxian[number][2] = max(huaxian[number-1][2], huaxian[number][2])
    output_set.append(tuple(huaxian[-1]))
    return output_set

"""
1. 不要修改输入数据
2. 不要不遵守输入输出约定, 可以在过程中暂时改成list，但是要记得改回tuple
3. 注意空格
"""
