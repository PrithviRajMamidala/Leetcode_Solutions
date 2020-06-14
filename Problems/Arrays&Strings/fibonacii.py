def fib(N):
    lst = []
    lst.append(0)
    lst.append(1)

    for i in range(2, N+1):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst[N]

if __name__ == '__main__':
    print(fib(5))

