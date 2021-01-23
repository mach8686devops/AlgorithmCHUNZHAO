# 有效的字母异位词
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # return sorted(s)==sorted(t)
