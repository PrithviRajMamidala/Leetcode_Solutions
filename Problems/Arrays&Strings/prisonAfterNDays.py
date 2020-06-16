def prisonAfterNDays(cells, N):
    Res = [1]*8
    Res[0] = 0
    Res[7] = 0
    days = 1
    while days <= N:

        for i in range(1, 7):
            if cells[i-1] == cells[i+1]:
                Res[i] = 1
            else:
                Res[i] = 0

        cells = Res
        days += 1
    return Res



if __name__ == '__main__':
    print(prisonAfterNDays([0,1,0,1,1,0,0,1], 7))