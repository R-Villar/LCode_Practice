from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if a list contains any duplicate elements.

    Args:
        nums (List[int]): The list of integers to check for duplicates.

    Returns:
        bool: True if the list contains duplicates, False otherwise.
    """
    hash_set = set()

    for number in nums:
        if number in hash_set:
            return True
        hash_set.add(number)

    return False


num = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# num = [1,2,3,3]
print(contains_duplicate(num))
