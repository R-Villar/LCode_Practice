from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Finds two numbers in the given list that add up to the target value.

    Args:
        nums (List[int]): The list of numbers to search for pairs.
        target (int): The target value to find the sum of two numbers.

    Returns:
        List[int]: A list containing the indices of the two numbers that add up to the target value.
        If no such pair is found, an empty list is returned.
    """
    value_to_index_map = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in value_to_index_map:
            return [value_to_index_map[diff], i]
        value_to_index_map[n] = i
    return []


print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))
