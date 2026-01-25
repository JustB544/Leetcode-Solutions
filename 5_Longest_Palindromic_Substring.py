'''
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        best : str = s[0]

        # handle edge cases that while loop won't catch
        if (len(s) == 1):
            return best
        if (s[0] == s[1]):
            best = s[:2]

        # search through seed pairs. even is (\w)\w\1, and odd is (\w)\1
        def search(n: int, even : bool) -> str:
            l : int = n-1
            r : int = n+2 if even else n+1
            while (l >= 0 and r < len(s)):
                if (s[l] != s[r]):
                    return s[l+1:r]
                l -= 1
                r += 1
            return s[l+1:r]
        # return the string that is the longest (or the first if equal)
        def max_str(s1 : str, s2: str) -> str:
            if (len(s1) >= len(s2)):
                return s1
            return s2

        # check track of last two characters
        prev_arr : list[str] = [s[0], s[1]]
        # iterate through string, searching from each possible palindrome center
        for n in range(2, len(s)):
            # checks odd palindromes
            if (s[n] == prev_arr[0]):
                best = max_str(best, search(n-1, False))
            # checks even palindromes
            if (s[n] == prev_arr[1]):
                best = max_str(best, search(n-1, True))
            prev_arr[0] = prev_arr[1]
            prev_arr[1] = s[n]
        return best