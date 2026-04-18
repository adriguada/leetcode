class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        num_vowels = 0

        for c in s[:k]:
            if self.isVowel(c):
                num_vowels += 1

        max_vowels = num_vowels

        for i in range(k, len(s)):
            if self.isVowel(s[i]):
                num_vowels += 1
            if self.isVowel(s[i - k]):
                num_vowels -= 1

            max_vowels = max(max_vowels, num_vowels)

        return max_vowels

    def isVowel(self, s: str) -> bool:
        return s in "aeiouAEIOU"
