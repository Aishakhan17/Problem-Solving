def two_sum(arr, target):
    valueToIndex = {}
    for i in range(len(arr)):
        if arr[i] not in valueToIndex:
            valueToIndex[arr[i]] = i
        pair = target - arr[i]
        if pair in valueToIndex and valueToIndex[pair] != i:
            return valueToIndex[pair], i


# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([3, 2, 4], 6))
# print(two_sum([3, 3], 6))


def two_sum_sorted(arr, target):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == target:
            return i, j
        elif arr[i] + arr[j] < target:
            i += 1
        elif arr[i] + arr[j] > target:
            j -= 1


two_sum_sorted([1, 2, 4, 7, 11, 15], 15)
two_sum_sorted([5, 6, 9, 12, 15, 21], 21)
two_sum_sorted([21, 24, 26, 29, 32, 35], 50)
