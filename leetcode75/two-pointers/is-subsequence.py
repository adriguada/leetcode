class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pt = 0
        for t_pt in range(len(t)):
            if s_pt >= len(s):
                return True
            elif t[t_pt] == s[s_pt]:
                s_pt += 1

        return s_pt >= len(s)
