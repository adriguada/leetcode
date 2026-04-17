from typing import List

"""
Solution: Two-pointer approach.

The idea is to start with the widest container and move the pointers inward,
by moving the one pointing to the shorter line towards the center.

The lower line is the bottleneck for the container's capacity.
Moving the greater line will always obtain a smaller or equal area.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0

        left = 0
        right = len(height) - 1

        while left < right:
            x = right - left
            y = min(height[left], height[right])
            area = x * y
            ans = max(ans, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans
