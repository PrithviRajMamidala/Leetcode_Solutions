def partitionLabels(S):
    last = {c: i for i, c in enumerate(S)}
    print(last)
    j = anchor = 0
    ans = []
    for i, c in enumerate(S):
        print(i, c)
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
    return ans

if __name__ == '__main__':
    print(partitionLabels("ababcbacadefegdehijhklij"))
