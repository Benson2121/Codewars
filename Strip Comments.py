def solution(string,markers):
    split1=string.split('\n')
    for num,i in enumerate(split1):
        for j in markers:
            if split1[num].find(j) !=-1:
                if split1[num].find(j)==0:
                    split1[num]=''
                else:
                    split1[num]=split1[num][:split1[num].index(j)-1].rstrip()
    return '\n'.join(split1)
