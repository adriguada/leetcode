from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summatory = sum(nums[:k])
        max_sum = summatory

        for i in range(k, len(nums)):
            summatory -= nums[i - k]
            summatory += nums[i]

            max_sum = max(max_sum, summatory)

        return max_sum / k
