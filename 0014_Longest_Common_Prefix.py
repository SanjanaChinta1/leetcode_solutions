# Problem: Longest Common Prefix
# LeetCode: 14
# Difficulty: Easy
# Language: Python
# Approach: Sorting
# Time Complexity: O(n log n + m)
# Space Complexity: O(1) auxiliary space

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        strs.sort()

        i = 0

        while i < len(strs[0]):
            if strs[0][i] == strs[-1][i]:
                ans = ans + strs[0][i]
            else:
                break

            i += 1

        return ans
