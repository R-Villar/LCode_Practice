def longestConsecutive(nums):
    numSet = set(nums)
    longestSequence = 0
    length = 0

    for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            while n + length in numSet:
                length += 1
            longestSequence = max(length, longestSequence)
    return longestSequence


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
