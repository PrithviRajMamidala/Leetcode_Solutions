def prisonAfterNDays(cells, N):

    temp = N
    lst = []
    if N != 0:
        b = []

        for i in range(len(cells)):
            if i == 0 or i == len(cells) - 1:
                b.append(0)
            else:
                if cells[i - 1] == cells[i + 1]:
                    b.append(1)
                else:
                    b.append(0)
        if temp == N:
            lst = b
        N = N - 1
        print(lst)
        cells = b
        # print(cells)
        return prisonAfterNDays(cells, N)
    # print(lst)
    return cells


if __name__ == '__main__':
    print(prisonAfterNDays([0,1,0,1,1,0,0,1], 7))
    # print(prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))