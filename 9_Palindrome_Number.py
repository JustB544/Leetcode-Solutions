'''
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check if negative
        if x < 0:
            return False
        # check if the same backwards
        return str(x) == str(x)[::-1]