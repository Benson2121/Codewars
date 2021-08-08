def next_smaller(n):
    list1=list(str(n))
    list2=[list1[-1]]
    if sorted(list1)==list1:
        return -1
    
    for i in range(1,len(list1)):
        list2.append(list1[-i-1])
        list2.sort(reverse=True)
        if list1[-i]<list1[-i-1]:
            k=max(j for j in list2 if j<list1[-i-1])
            list1[-i-1]=k
            list2.remove(k)
            list1=list1[:-i]
            list1=list1+list2
            break
        
    if list1[0]=='0' or int(''.join(list1))==n:
        return -1
    return int(''.join(list1))
