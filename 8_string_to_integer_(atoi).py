class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        minus = False
        if len(s) == 0:
            return 0
        if s[0] == '-':
            minus = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        if len(s) == 0:
            return 0
        if not s[0].isdigit():
            return 0
        x = ''
        for i in s:
            if i.isdigit():
                x += str(i)
            else:
                break
        xx = int(x)
        if minus:
            xx *= -1
        if xx > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if xx < -2 ** 31:
            return -2 ** 31
        return xx

        # import re
        # x = re.sub('[A-Za-z+. ]', '', s)
        # xx = int(x)
        # if xx > 2 ** 31 - 1:
        #     return 2 ** 31 - 1
        # if xx < -2 ** 31:
        #     return -2 ** 31
        # return xx


print(Solution().myAtoi("sdf -123 sdf dsf ."))
print(Solution().myAtoi("   -123 sdf dsf ."))
print(Solution().myAtoi("   123 sdf dsf ."))
print(Solution().myAtoi("42"))
print(Solution().myAtoi("sdfsdf"))
print(Solution().myAtoi(""))
