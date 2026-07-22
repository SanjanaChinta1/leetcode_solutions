# Problem: Maximum Points You Can Obtain from Cards
# LeetCode: 1423
# Difficulty: Medium
# Language: Python
# Approach: Sliding Window / Prefix-Suffix Sum
# Time Complexity: O(k)
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = sum(cardPoints[0:k])
        ans = left_sum
        right_sum = 0

        for i in range(1, k + 1):
            left_sum -= cardPoints[k - i]
            right_sum += cardPoints[-i]
            ans = max(left_sum + right_sum, ans)

        return ans