# Problem: Jump Game
# LeetCode: 55
# Difficulty: Medium
# Language: Python
# Approach: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i, jump in enumerate(nums):
            # If current index is beyond the farthest reachable position
            if i > max_reach:
                return False

            # Update the farthest position we can reach
            max_reach = max(max_reach, i + jump)

            # We can already reach the last index
            if max_reach >= len(nums) - 1:
                return True

        return max_reach >= len(nums) - 1