# Problem: Pow(x, n)
# LeetCode: 50
# Difficulty: Medium
# Approach: Binary Exponentiation / Recursion
# Time Complexity: O(log n)
# Space Complexity: O(log n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        if n % 2 == 1:
            return x * half * half
        return half * half
