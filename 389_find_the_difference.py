class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        for x in s:
            t.remove(x)
        return t[0]


print(Solution().findTheDifference(s="abcd", t="abcde"))

'''
    return list(set(t)-set(s))[0]
'''
