from collections import defaultdict
from typing import List


def group_anagram(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)  # mapping charCount to list of anagrams

    for s in strs:
        count = [0] * 26  # a ... z

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    return res.values()


print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagram([""]))
print(group_anagram(["a"]))
