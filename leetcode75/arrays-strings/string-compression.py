from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        c = ""
        counter = 0

        i = 0
        j = 0
        while i < len(chars):
            c = chars[i]

            counter = 0
            while i < len(chars) and chars[i] == c:
                counter += 1
                i += 1

            chars[j] = c
            j += 1
            if counter > 1:
                for num in str(counter):
                    chars[j] = num
                    j += 1

        return j
