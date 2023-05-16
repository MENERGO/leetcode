class Solution:
    def countAndSay(self, n: int) -> str:
        def say(x: str) -> str:
            if x == '0':
                return '1'
            str_n: str = ''
            k: int = 0
            prev: str = ''
            for nn, i in enumerate(x):
                if i == prev and nn == len(x) - 1:
                    k += 1
                    str_n += str(k) + prev
                elif i == prev:
                    k += 1
                else:
                    if prev == '' and nn == len(x) - 1:
                        k += 1
                        str_n += str(k) + i
                    elif prev == '':
                        prev = i
                        k = 1
                    elif nn == len(x) - 1:
                        str_n += str(k) + prev
                        k = 1
                        prev = i
                        str_n += str(k) + prev
                    else:
                        str_n += str(k) + prev
                        k = 1
                        prev = i
            return str_n

        y: str = '0'
        for count in range(n):
            y = say(y)
        return y


'''
        if n == 1:
            return '1'
        x = self.countAndSay(n - 1)
        currChar = x[0]
        currCounter = 0
        res = ''
        for i in x:
            if i == currChar:
                currCounter += 1
            else:
                res += str(currCounter) + currChar
                currCounter = 1
                currChar = i
        res += str(currCounter) + currChar
        return res
'''

print(Solution().countAndSay(6))
