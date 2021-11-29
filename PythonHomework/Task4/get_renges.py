def get_ranges(l):
    new_l = []
    try:
        for i in range(len(l)):
            if l[i+1] != l[i]+1 and l[i] != l[i-1]+1:
                new_l.append(str(l[i]))
            if l[i+1] == l[i]+1 and l[i] != l[i-1]+1:
                for k in range(i, len(l)-1):
                    if l[k+1] != l[k]+1:
                        new_l.append(f"{l[i]}-{l[k]}")
                        i = k
                        break
                if l[-1] == l[-2]+1:
                    for t in range(len(l)-1, i, -1):
                        if l[t] != l[t-1]+1:
                            new_l.append(f"{l[i+1]}-{l[t+1]}")
                            break
    except IndexError:
        if l[-1] != l[-2]+1:
            new_l.append(str(l[-1]))
    return ", ".join(new_l)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
