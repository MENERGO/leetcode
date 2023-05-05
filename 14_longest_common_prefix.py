class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pref: str = ''
        for n in range(len(min(strs))):
            x: str = strs[0][n]
            for i in strs:
                if i[n] != x:
                    return pref
            pref += x
        return pref


print(Solution().longestCommonPrefix(strs=["ab", "a"]))
