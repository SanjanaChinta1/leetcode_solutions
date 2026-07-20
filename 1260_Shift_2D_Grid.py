# Problem: Shift 2D Grid
# LeetCode: 1260
# Difficulty: Easy
# Language: Python
# Time Complexity: O(m × n)
# Space Complexity: O(m × n)

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        tot = m * n

        # Flatten the 2D grid into a 1D list
        flat = []
        for row in grid:
            for val in row:
                flat.append(val)

        # Reduce unnecessary shifts
        k = k % tot

        # Perform the shift
        shifted = flat[-k:] + flat[:-k]

        # Convert back to a 2D grid
        result = []
        for i in range(0, tot, n):
            result.append(shifted[i:i + n])

        return result