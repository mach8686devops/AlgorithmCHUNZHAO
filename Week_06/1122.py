from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def mycmp(x: int) -> (int, int):
            return rank[x] if x in rank else x

        n = len(arr2)
        rank = {x: i - n for i, x in enumerate(arr2)}
        arr1.sort(key=mycmp)
        return arr1
