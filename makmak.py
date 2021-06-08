def upperAver(score):
    sum = 0
    count =  0
    for i in range(len(list)):
        sum += list[i]
    aver = sum / len(list)
    for i in score:
        if i >= aver:
            count += 1

    return count

