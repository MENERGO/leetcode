class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alf = [v.upper() for v in list(map(chr, range(97, 123)))]
        len_alf = len(alf)
        result = ''
        while columnNumber > 0:
            columnNumber -= 1
            result = alf[columnNumber % len_alf] + result
            columnNumber //= len_alf
        return result
