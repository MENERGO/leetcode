class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        result = []
        d = {i: n + 1 for n, i in enumerate(sorted(score, reverse=True))}
        for i in score:
            x = str(d[i])
            if x == '1':
                x = 'Gold Medal'
            elif x == '2':
                x = 'Silver Medal'
            elif x == '3':
                x = 'Bronze Medal'
            result.append(x)
        return result
