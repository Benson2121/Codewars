def dbl_linear(n):
    list1=[1]
    for i in range(10*n):
        list1.append(list1[i]*2+1)
        list1.append(list1[i]*3+1)
    list1=sorted(set(list1))
    return list1[n]
