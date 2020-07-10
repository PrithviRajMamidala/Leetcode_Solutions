# using for loop
def removeElement(nums, val):
    l = nums.count(val)
    for i in range(l):
        nums.remove(val)
    print(nums)
    return len(nums)


# using recursive function
def removeElement_1(nums, val):
    if val in nums:
        nums.remove(val)
        return removeElement(nums, val)

    print(nums)

    return len(nums)

def removeElement_2(nums, val):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n-1]
            n -= 1
        else:
            i += 1
    return n

if __name__ == '__main__':
    print(removeElement_2([0,1,2,2,3,0,4,2], 2))