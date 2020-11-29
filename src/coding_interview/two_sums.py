def two_nums(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        # print(i, v)
        remaining = target - v
        if remaining in seen:
            return [seen[remaining], i]
        seen[v] = i

    return []


print(two_nums([2, 7, 11, 15], 9))
