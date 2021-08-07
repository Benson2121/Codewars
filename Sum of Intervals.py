def sum_of_intervals(intervals):
    a=[]
    for i in intervals:
        for i in range(i[0],i[1]):
            if i not in a:
                a.append(i)
    return len(a)
