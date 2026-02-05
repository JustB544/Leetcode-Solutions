'''
3637. Trionic Array I

You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.
'''
class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        # store the current phase of the trionic
        phase : int = 0
        prev : int = nums[0]
        # store phase length to make sure first phase is established
        phase_len : int = 0
        # loop through nums, starting with the second index
        for n in nums[1:]:
            # check if entering next phase or breaking the trionic pattern
            if ((phase == 0 and n <= prev) or (phase == 1 and n >= prev) or (phase == 2 and n <= prev)):
                # return false if 2 consecutive are equal, entering the 3rd phase, or if first phase isn't established
                if (n == prev or phase == 2 or (phase == 0 and phase_len == 0)):
                    return False
                phase += 1
                phase_len = -1
            phase_len += 1
            prev = n
        # return true only if the trionic is completed
        if (phase == 2):
            return True
        return False