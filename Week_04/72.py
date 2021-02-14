from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache
        def dp(i, j):
            if i * j == 0:
                return i + j
            return dp(i - 1, j - 1) if word1[i - 1] == word2[j - 1] else min(dp(i - 1, j),
                                                                             dp(i, j - 1),
                                                                             dp(i - 1, j - 1)) + 1

        return dp(len(word1), len(word2))
