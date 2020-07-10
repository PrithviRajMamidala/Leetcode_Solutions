def arrangeCoins(n):
    count = 0
    step = 0

    for i in range(1, n+1):
        count += i
        if count <= n:
            step += 1
        else:
            return step
    return step

if __name__ == '__main__':
    print(arrangeCoins(1))