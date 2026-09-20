# Problem: Reverse Degree of a String
# LeetCode: 3498
# Difficulty: Easy
# Language: Python
# Approach: ASCII / Character Value Calculation
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, c in enumerate(s):
            reverse_val = 26 - (ord(c) - ord('a'))
            pos = i + 1
            total += reverse_val * pos
        return total
