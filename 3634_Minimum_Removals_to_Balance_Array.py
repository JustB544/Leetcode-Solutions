'''
3634. Minimum Removals to Balance Array

You are given an integer array nums and an integer k.

An array is considered balanced if the value of its maximum element is at most k times the minimum element.

You may remove any number of elements from nums​​​​​​​ without making it empty.

Return the minimum number of elements to remove so that the remaining array is balanced.

Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.
'''
class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums.sort()
        l : int = 0
        r : int = -1
        best : int = len(nums)-1
        for i in range(1, len(nums)):
            l += 1
            if (nums[i] >= nums[-1] / k):
                break
        best = min(l, best)
        while (l > 0):
            l -= 1
            while ((l - r - 1 < len(nums)) and nums[l] * (nums[-1] / nums[r]) < nums[-1] / k):
                r -= 1
            best = min(l - r - 1, best)
        return best