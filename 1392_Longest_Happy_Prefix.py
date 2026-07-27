# Problem: Longest Happy Prefix
# LeetCode: 1392
# Difficulty: Hard
# Language: Python
# Approach: KMP (Longest Prefix Suffix - LPS)
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lsp = [0] * n
        i, j = 0, 1

        while j < n:
            if s[i] == s[j]:
                i += 1
                lsp[j] = i
                j += 1
            else:
                if i == 0:
                    lsp[j] = 0
                    j += 1
                else:
                    i = lsp[i - 1]

        if lsp[n - 1] == 0:
            return ""

        start = n - lsp[n - 1]
        return s[start:]