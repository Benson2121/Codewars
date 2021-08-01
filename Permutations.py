def permutations(string):
    sum1=[]
    if len(list(set(list(string))))==1:
        return [string]
    for i in list(set(list(string))):
        n=list(string)
        n.remove(i)
        for j in permutations(''.join(n)):
            k=i+j
            sum1=sum1+[k]
    return sum1
