from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = zeros = max_ones = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_ones = max(max_ones, right - left)

        return max_ones
