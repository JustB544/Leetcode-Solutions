'''
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''
class Solution:
    def reverse(self, x: int) -> int:
        _x : str | int = ""
        # check for negative sign
        negative : bool = x < 0
        # reverse digits using a string
        _x = str(abs(x))[::-1]
        # convert back to integer
        _x = -int(_x) if negative else int(_x)
        # check if out of range
        if (_x > 2**31 - 1 or _x < -2**31):
            return 0
        return _x