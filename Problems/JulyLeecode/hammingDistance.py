def hammingDistance(x, y):
    if not 0 <= x < (2 ** 31) and 0 <= y < (2 ** 31):
        return 0

    temp = bin(x ^ y)
    return temp.count('1')


if __name__ == '__main__':
    print(hammingDistance(1, 4))