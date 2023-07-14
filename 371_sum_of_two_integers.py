class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0 and a != b:
            return b
        elif b == 0 and a != b:
            return a
        elif b == 0 and a == b:
            return 0
        result = []
        if a < 0 and b < 0:
            for i in range(abs(a)):
                result.append(1)
            for i in range(abs(b)):
                result.append(1)
            return f'-{result.count(1)}'
        if a > 0 and b > 0:
            for i in range(a):
                result.append(1)
            for i in range(b):
                result.append(1)
            return result.count(1)
        if abs(a) == abs(b):
            return 0
        if a < 0:
            a, b = b, a
        if abs(a) > abs(b):
            for i in range(a):
                result.append(1)
            for i in range(abs(b)):
                result.remove(1)
            return result.count(1)
        else:
            for i in range(abs(b)):
                result.append(1)
            for i in range(abs(a)):
                result.remove(1)
            return f'-{result.count(1)}'


print(Solution().getSum(a=2, b=3))
