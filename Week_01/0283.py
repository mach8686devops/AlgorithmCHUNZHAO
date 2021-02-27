# 移动零


class Solution(object):
    def moveZeroes(self, n):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # idxs = [idx for idx , num in enumerate(nums) if num == 0]
        # for i in idxs[::-1]:
        #     nums.pop(i)
        # nums += len(idxs) *[0]
        j = 0
        for i in range(len(n)):
            if n[i] != 0:
                n[j], n[i] = n[i], n[j]
                j += 1
