
def checkBoundaries(row, col, peri, x):

    if col - 1 == -1 or x[row][col - 1] == 0:
        peri += 1
    if col + 1 == 4 or x[row][col + 1] == 0:
        peri += 1
    if col - 1 == -1 or col + 1 == 4 or x[row][col - 1] == 1 or x[row][col + 1] == 1:
        pass

    if row - 1 == -1 or x[row-1][col] == 0:
        peri += 1
    if row + 1 == 4 or x[row+1][col] == 0:
        peri += 1
    if row - 1 == -1 or row + 1 == 4 or x[row-1][col] == 1 or x[row+1][col] == 1:
        pass

    return peri


def islandPerimeter(grid):
    perimeter = 0
    temp = -1

    for i in grid:
        temp += 1
        for j in i:
            if j == 1:
                perimeter = checkBoundaries(temp, j, perimeter, grid)

    return perimeter

if __name__ == '__main__':
    print(islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))