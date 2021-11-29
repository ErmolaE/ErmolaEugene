def sum_subl(l):
    total = 0
    for i in l:
        if (type(i) == type([])):
            total = total + sum_subl(i)
        else:
            total = total + i
    return total

l = [1, 2, [2, 4, [[7, 8], 4, 6]]]

if __name__ == '__main__':
    print(sum_subl(l))
