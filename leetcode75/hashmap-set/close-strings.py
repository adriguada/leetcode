class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        chars1 = {}
        chars2 = {}

        freqs1 = {}
        freqs2 = {}

        op1 = True

        for c in word1:
            chars1[c] = chars1.get(c, 0) + 1
        for c in word2:
            chars2[c] = chars2.get(c, 0) + 1

        if chars1.keys() != chars2.keys():
            return False

        for c in chars1:
            if chars1[c] != chars2[c]:
                op1 = False

        op2 = True

        for freq in chars1.values():
            freqs1[freq] = freqs1.get(freq, 0) + 1

        for freq in chars2.values():
            freqs2[freq] = freqs2.get(freq, 0) + 1

        if freqs1.keys() != freqs2.keys():
            return False

        for f in freqs1:
            if freqs1[f] != freqs2[f]:
                op2 = False

        return op1 or op2
