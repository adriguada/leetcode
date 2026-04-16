from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preffixes = [0] * len(nums)
        suffixes = [0] * len(nums)
        answer = [0] * len(nums)

        preffix = 1
        for i in range(len(preffixes)):
            preffixes[i] = preffix
            preffix *= nums[i]

        suffix = 1
        for i in range(len(suffixes) - 1, -1, -1):
            suffixes[i] = suffix
            suffix *= nums[i]

        for i in range(len(nums)):
            answer[i] = preffixes[i] * suffixes[i]

        return answer
