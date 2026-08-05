# Problem: Fruit Into Baskets
# LeetCode: 904
# Difficulty: Medium
# Language: Python
# Approach: Sliding Window + Hash Map
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        count = {}
        ans = 0

        for right in range(len(fruits)):
            # Add the current fruit to the window
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            # Shrink the window until it contains at most 2 fruit types
            while len(count) > 2:
                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            # Update the maximum number of fruits collected
            ans = max(ans, right - left + 1)

        return ans