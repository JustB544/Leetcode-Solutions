'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ld : dict = {}
        i : int = 0
        # create index lookup dictionary for each value
        for x in nums:
            ld[x] = i
            i += 1
        i = 0
        # for each value check if the needed value is in the dictionary, and that it isn't itself
        for x in nums:
            if (target-x in ld and i != ld[target-x]):
                return [i, ld[target-x]]
            i += 1
        return False
        