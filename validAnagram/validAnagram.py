def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    Args:
        s (str): The first input string.
        t (str): The second input string.

    Returns:
        bool: True if the two input strings are anagrams of each other, False otherwise.
    """
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True


word = "anagram"
target = "nagaram"

is_anagram(word, target)
