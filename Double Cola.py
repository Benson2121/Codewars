def who_is_next(names, r):
    move=len(names)
    constant=2
    sum=0
    if r<move:
        return names[r-1]
    while sum+move*2<r:
        sum=sum+move*2
        move=move*2
        constant=2*constant
    k=r-sum
    if k%constant==0:
        return names[k//constant-1]
    else:
        print(r,sum,k,constant)
        return names[k//constant]
    
who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52)
