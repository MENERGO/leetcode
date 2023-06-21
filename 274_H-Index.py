class Solution:
    def hIndex(self, citations: list[int]) -> int:
        if len(citations) == 0:
            return 0
        citations = sorted(citations, reverse=True)
        for n, h in enumerate(citations):
            if n + 1 > h:
                return n
        return len(citations)


print(Solution().hIndex([3, 0, 6, 1, 5]))
