class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1

        s_list = list(s)

        while i < j:
            if not self.isVowel(s_list[i]):
                i += 1
            elif not self.isVowel(s_list[j]):
                j -= 1
            else:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1

        return "".join(s_list)               
    
    def isVowel(self, char: str) -> bool:
        return char in "aeiouAEIOU"