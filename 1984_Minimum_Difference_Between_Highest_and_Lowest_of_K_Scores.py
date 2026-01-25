'''
1984. Minimum Difference Between Highest and Lowest of K Scores

You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.
'''
class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        # sort array to guarantee minimal difference between numbers
        nums.sort()
        # set initial min_diff at the max difference between elements
        min_diff : int = nums[-1] - nums[0]
        # iterate through k-length windows, and find the minimal difference between the first and last element in the window
        for x in range(len(nums)-k+1):
            min_diff = min(min_diff, nums[x+k-1]-nums[x])
        return min_diff