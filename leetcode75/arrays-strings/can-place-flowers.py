from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (
                not flowerbed[i] # el plot actual está vacío
                and (i == 0 or not flowerbed[i-1]) # el plot anterior está vacío o no hay plot anterior
                and (i == len(flowerbed)-1 or not flowerbed[i+1]) # el plot siguiente está vacío o no hay plot siguiente
            ):
                flowerbed[i] = 1
                n -= 1
        return n <= 0