class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        alf = {v.upper(): n + 1 for n, v in enumerate(list(map(chr, range(97, 123))))}
        result = 0
        for n, i in enumerate(columnTitle[::-1]):
            result += 26 ** n * alf[i]
        return result


print(Solution().titleToNumber("A"))
