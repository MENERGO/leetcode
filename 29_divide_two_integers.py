class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        minus = False
        if '-' in str(divisor) and '-' in str(dividend):
            pass
        elif not str(divisor)[0].isdigit():
            divisor = int(str(divisor).lstrip('-'))
            minus = True
        elif '-' in str(dividend):
            dividend = int(str(dividend).lstrip('-'))
            minus = True
        k = divmod(dividend, divisor)[0]
        if minus:
            k = int('-' + str(k))
        if k > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if k < -2 ** 31:
            return -2 ** 31
        return k


print(Solution().divide(dividend=7, divisor=-3))
