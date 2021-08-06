def count_change(money, coins):
    # your implementation here
    k=0
    if money < min(coins):
        return 0
    for i in coins:
        if money==i:
            return 1
        else:
            k=k+count_change(money-i,coins)
    return k
print(count_change(10,[5,2,3]))
