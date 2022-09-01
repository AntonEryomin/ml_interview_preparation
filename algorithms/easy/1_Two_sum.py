from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = dict()

        for idx in range(len(nums)):
            if target - nums[idx] in visited_nums:
                return [visited_nums[target - nums[idx]], idx]
            else:
                visited_nums[nums[idx]] = idx


# Memory Complexity: O(n)
# Time Complexity: O(n)