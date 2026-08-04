# Problem: Find Missing Elements
# LeetCode: 3731
# Difficulty: Easy
# Language: Python
# Approach: Linear Scan
# Time Complexity: O((max - min) × n)
# Space Complexity: O(k)
# (where k is the number of missing elements)

from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        result = []

        for i in range(mini + 1, maxi):
            if i not in nums:
                result.append(i)

        return result