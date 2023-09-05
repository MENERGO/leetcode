class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(set(s)) == 1 and len(s) != 1:
            return True
        if len(s) == 2:
            return False
        for i in range(2, len(s)):
            if len(s) % i == 0:
                if len(set([s[x:x + i] for x in range(0, len(s), i)])) == 1:
                    return True
        return False
