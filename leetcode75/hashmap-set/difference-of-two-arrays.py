from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        aSet = set()
        bSet = set()

        for num in nums1:
            aSet.add(num)
        for num in nums2:
            bSet.add(num)

        for num in nums1:
            if num in bSet:
                aSet.discard(num)
                bSet.discard(num)

        return [list(aSet), list(bSet)]
