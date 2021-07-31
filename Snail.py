def snail(snail_map):
    r=len(snail_map)-1
    s=0
    list1=[]
    while r!=-1 and r!=0:
        for i in range(s,s+r):
            list1.append(snail_map[s][i])
        for i in range(s,s+r):
            list1.append(snail_map[i][r+s])
        for i in range(r+s,s,-1):
            list1.append(snail_map[r+s][i])
        for i in range(r+s,s,-1):
            list1.append(snail_map[i][s])
        r=r-2
        s=s+1
    if r==0:
        try:
            list1.append(snail_map[s][s])
        except:
            return list1
    return list1
