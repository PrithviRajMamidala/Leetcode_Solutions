def plusOne(digits):
    b = ''
    for i in digits:
        b += str(i)
    res = str(int(b) + 1)
    digits.clear()
    for i in res:
        digits.append(int(i))

    return digits


if __name__ == '__main__':
    print(plusOne([9, 9]))