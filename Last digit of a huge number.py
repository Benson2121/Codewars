def last_digit(lst):
    lastDigit = 1

    for i in range(len(lst) - 1, -1, -1):
        if lastDigit == 0:
            lastDigit = 1
        elif lastDigit == 1:
            lastDigit = lst[i]
        else:
            lastDigit = lst[i]**(lastDigit%4+4)
    return lastDigit%10
