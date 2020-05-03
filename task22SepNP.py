def separate_p_m(numbers_list):
    pos = []
    neg = []
    for number in numbers_list:
        if number >= 0:
            pos.append(number)
        else:
            neg.append(number)
    return pos, neg

numbers_list = [-5,-4,-3,-2,-1,1,2,3,4,5]
pos, neg = separate_p_m(numbers_list)
print(pos)
print(neg)