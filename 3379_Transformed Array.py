'''
3379. Transformed Array

You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:

For each index i (where 0 <= i < nums.length), perform the following independent actions:
If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
If nums[i] == 0: Set result[i] to nums[i].
Return the new array result.
'''
class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        result : list[int] = [0] * len(nums)
        # set result to nums at i + nums[i] mod length of nums
        for i in range(len(nums)):
            result[i] = nums[(i+nums[i])%len(nums)]
        return result