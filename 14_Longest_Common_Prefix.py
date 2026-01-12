'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        _str : str = strs[0]
        for i in strs[1:]:
            while (i[:len(_str)] != _str):
                _str = _str[:-1]
                if (len(_str) == 0):
                    return ""
        return _str