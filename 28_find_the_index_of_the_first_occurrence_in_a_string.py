class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        import re
        lst = [(m.start(0), m.end(0)) for m in re.finditer(needle, haystack)]
        if len(lst) == 0:
            return -1
        return lst[0][0]


print(Solution().strStr(haystack="hello", needle="ll"))
