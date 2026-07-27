# Problem: Maximum Product of Two Elements in an Array
# LeetCode: 1464
# Difficulty: Easy
# Language: Python

# -----------------------------
# Approach 1: Brute Force
# Time Complexity: O(n²)
# Space Complexity: O(1)
# -----------------------------

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    maxi = max(maxi, (nums[i] - 1) * (nums[j] - 1))

        return maxi


# -----------------------------
# Approach 2: Optimized
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)