# Problem: Longest Subsequence With Non-Zero XOR
# LeetCode: 3702
# Difficulty: Medium
# Language: Python
# Approach: XOR / Bit Manipulation
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0

        # Calculate XOR of all elements
        for num in nums:
            total_xor ^= num

        # If total XOR is non-zero, take the entire array
        if total_xor != 0:
            return len(nums)

        # If all elements are zero, no valid subsequence exists
        if all(num == 0 for num in nums):
            return 0

        # Otherwise, remove one non-zero element
        return len(nums) - 1