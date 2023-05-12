class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            len_s = len(s)
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
            if len_s == len(s):
                break
        if len_s != 0:
            return False
        return True


print(Solution().isValid(s='()[]{}'))
