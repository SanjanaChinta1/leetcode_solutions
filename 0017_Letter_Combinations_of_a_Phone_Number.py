# Problem: Letter Combinations of a Phone Number
# LeetCode: 17
# Difficulty: Medium
# Language: Python
# Approach: Backtracking
# Time Complexity: O(4^n)
# Space Complexity: O(n)

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(index, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return

            letters = mapping[digits[index]]
            for c in letters:
                backtrack(index + 1, cur + c)

        backtrack(0, "")
        return res
