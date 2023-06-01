class Solution:
    def isHappy(self, n: int) -> bool:
        results = [n]
        while True:
            list_n = list(map(int, list(str(n))))
            pre = sum([x ** 2 for x in list_n])
            if pre == 1:
                return True
            if pre in results:
                return False
            results.append(pre)
            n = pre


print(Solution().isHappy(19))
