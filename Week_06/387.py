from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = Counter(s)  # 使用字典
        for i in range(len(s)):
            if dic[s[i]] == 1:  # 如果字典中value为1
                return i
        return -1
