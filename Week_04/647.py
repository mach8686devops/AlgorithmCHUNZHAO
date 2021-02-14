class Solution(object):
    cnt = 0

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_index = 0
        for _ in s:
            self.extendSubstrings(s_index, s_index, s)
            self.extendSubstrings(s_index, s_index + 1, s)
            s_index = s_index + 1
        return self.cnt

    def extendSubstrings(self, start, end, s):
        while (start >= 0 and end < len(s)) and (s[start] == s[end]):
            start = start - 1
            end = end + 1
            self.cnt = self.cnt + 1
