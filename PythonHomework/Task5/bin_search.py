def binary_search(x, l):
    left = 0
    right = len(l)-1
    mid = (left + right)//2
    if (x == l[mid]):
        return mid
    if (x > l[mid]):
        return binary_search(x, l[mid+1:]) + (mid + 1)
    return binary_search(x, l[:mid])


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 8

if __name__ == '__main__':
    print(binary_search(x, l))
