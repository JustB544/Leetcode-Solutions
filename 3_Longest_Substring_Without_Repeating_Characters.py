'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur : str = ""
        best : int = 0
        # iterate through s and add to cur until duplicate
        for x in s:
            if (cur.find(x) == -1):
                cur += x
            # increase best if higher, and reset cur to have 
            # everything after the first duplicate
            else:
                best = max(best, len(cur))
                cur = cur[cur.find(x)+1:] + x
        best = max(best, len(cur))
        return best