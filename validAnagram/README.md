## Summary
The `is_anagram` function checks if two input strings are anagrams of each other.

## Example Usage
```python
is_anagram("listen", "silent")
```
Output: True

## Code Analysis
### Inputs
- `s` (str): The first input string.
- `t` (str): The second input string.
___
### Flow
1. Check if the lengths of the two input strings are equal. If not, return False.
2. Create two empty dictionaries, `countS` and `countT`, to store the count of each character in the strings.
3. Iterate through each character in the first string `s` and update the count in `countS` dictionary.
4. Iterate through each character in the second string `t` and update the count in `countT` dictionary.
5. Compare the counts of each character in `countS` and `countT` dictionaries. If any count is different, return False.
6. If all counts are equal, return True.
___
### Outputs
- `True` if the two input strings are anagrams of each other.
- `False` if the two input strings are not anagrams of each other.
___
