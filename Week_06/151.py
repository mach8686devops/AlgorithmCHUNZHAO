class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(filter(lambda x: x != '', s.split(' ')))
        l.reverse()
        return ' '.join(l)
