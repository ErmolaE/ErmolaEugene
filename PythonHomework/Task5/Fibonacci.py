def fib_number(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_number(n-1) + fib_number(n-2)

def fib(n): 
    return [fib_number(i) for i in range(n)]

if __name__ == '__main__':
    print(fib(5))
    print(fib(10))
