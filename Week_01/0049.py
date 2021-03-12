class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) < 2:
            return [strs]
        ans = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            ans[key] = ans.get(key, []) + [s]
        return list(ans.values())


print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
