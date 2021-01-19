# 两个指针 都从尾部出发 可以这么理解

class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if A[i] >= B[j]:
                A[idx] = A[i]
                i -= 1
            else:
                A[idx] = B[j]
                j -= 1

            idx -= 1

        if i == -1:
            while j >= 0:
                A[j] = B[j]
                j -= 1
