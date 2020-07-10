def nthUglyNumber(n):
    Res = [1]
    if n == 0:
        return 0
    i, j, k = 0, 0, 0
    while len(Res) < n:
        min_num = min(Res[i] * 2, Res[j] * 3, Res[k] * 5)
        Res.append(min_num)
        if min_num == Res[i] * 2:
            i += 1
        if min_num == Res[j] * 3:
            j += 1
        if min_num == Res[k] * 5:
            k += 1

    return Res[n-1]



if __name__ == '__main__':
    print(nthUglyNumber(11))
