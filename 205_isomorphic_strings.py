class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        symbols = []
        for i in range(len(s)):
            if s[i] in symbols:
                continue
            ind_s = [index for index in range(len(s)) if s[index] == s[i]]
            ind_t = [index for index in range(len(t)) if t[index] == t[i]]
            if ind_t != ind_s:
                return False
            symbols.append(s[i])
        return True


print(Solution().isIsomorphic(s="egg", t="add"))
