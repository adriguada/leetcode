from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal, otherwise they won't have a common divisor
        if str1 + str2 != str2 + str1:
            return ""
        # The greatest common divisor string is the substring from 0 to gcd of size(str1), size(str2)
        return str1[: gcd(len(str1), len(str2))]
