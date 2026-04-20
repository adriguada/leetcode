from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums = dict()

        for num in arr:
            nums[num] = nums.get(num, 0) + 1
            # devuelve el valor de num en el dict, o 0 si no existe
        occurrences = set()

        for occ in nums.values():
            if occ in occurrences:
                return False
            else:
                occurrences.add(occ)

        return True
