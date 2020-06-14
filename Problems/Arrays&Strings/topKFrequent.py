from collections import Counter

def topKFrequent(nums, k):
    dict = {}
    for i in nums:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    sorted_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    Res = []
    for i in range(k):
        Res.append(sorted_items[i][0])
    return Res

def topKFrequent_1(nums, k):
    cnt = Counter(nums)
    sorted_items = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    Res = []
    for i in range(k):
        Res.append(sorted_items[i][0])
    return Res

if __name__ == '__main__':
    print(topKFrequent([1,1,1,2,2,3], 2))
    print(topKFrequent_1([1,1,1,2,2,3], 2))