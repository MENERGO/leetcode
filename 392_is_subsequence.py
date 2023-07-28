class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s == 0:
            return True
        if len_t == 0:
            return False
        i = 0
        x = ''
        for n in range(len_t):
            if s[i] == t[n]:
                x += t[n]
                if x == s:
                    return True
                i += 1
        return False


'''
        s_i, t_i = 0, 0
        while s_i < len(s) and t_i < len(t):
            s_i, t_i = s_i + (s[s_i] == t[t_i]), t_i + 1
        return s_i == len(s)
'''

print(Solution().isSubsequence(s="", t="ahbgdc"))
