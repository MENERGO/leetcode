class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        z = [1, 2, 3, 5]
        while n % 5 == 0 or n % 3 == 0 or n % 2 == 0:
            if n % 5 == 0:
                if n // 5 in z:
                    return True
                n = n // 5
            if n % 3 == 0:
                if n // 3 in z:
                    return True
                n = n // 3
            if n % 2 == 0:
                if n // 2 in z:
                    return True
                n = n // 2
        return False


print(Solution().isUgly(1))

'''
        if n == 1 or n == -1:
            return True
        if n % 5 == 0:
            if n // 5 == 3 or n // 5 == 2:
                return True
            n = n // 5
            if n // 3 == 2 or n // 2 == 3:
                return True
            return False
        if n % 3 == 0:
            if n // 3 == 2 or n // 3 == 5:
                return True
            n = n // 3
            if n // 2 == 5 or n // 5 == 2:
                return True
            return False
        if n % 2 == 0:
            if n // 2 == 3 or n // 2 == 5:
                return True
            n = n // 2
            if n // 3 == 5 or n // 5 == 3:
                return True
            return False
        return False
'''
