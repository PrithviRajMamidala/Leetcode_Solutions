def maxSubArray(nums):
    if len(nums) == 0:
        return 0

    this_dict = {}
    sum_arr = start = 0

    for i in range(len(nums)):
        if nums[i] in this_dict and start <= this_dict[nums[i]]:
            start = this_dict[nums[i]] + 1
        else:
            sum_arr = max(sum_arr, i - start + 1)
            this_dict[nums[i]] = i
    print(this_dict)
    return sum_arr

if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))