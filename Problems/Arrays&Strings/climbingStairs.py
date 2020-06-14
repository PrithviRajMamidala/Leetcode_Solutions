"""bottom-top approach
Can use dictionary for storing other elements and easy lookup more optimized solution"""

def climbStairs(n):
    stairs = []
    stairs.extend([0, 1, 2])
    # print(stairs)
    if n <= 2:
        return stairs[n]
    i = 3
    while i <= n:
        stairs.append(stairs[i-1] + stairs[i-2])
        i += 1

    return stairs[n]


if __name__ == '__main__':
    print(climbStairs(4))