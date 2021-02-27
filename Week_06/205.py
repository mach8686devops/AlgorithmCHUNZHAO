class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))
