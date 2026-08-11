# Problem: Missing Integer
# LeetCode: 2996
# Difficulty: Easy
# Language: Python
# Approach: Prefix Sum + Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]

        # Find the sum of the longest consecutive prefix
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find the smallest integer greater than or equal to
        # the prefix sum that is not present in nums
        seen = set(nums)

        answer = total

        while answer in seen:
            answer += 1

        return answer