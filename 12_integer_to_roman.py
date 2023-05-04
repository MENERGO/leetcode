class Solution:
    def intToRoman(self, num: int) -> str:
        def add_to_result(res, x, n):
            x: int = int(x)
            if x == 9:
                res = res + itr_2[9 * 10 ** n]
            elif x == 4:
                res = res + itr_2[4 * 10 ** n]
            else:
                f: int = x // 5
                e: int = x - 5 * f
                res = res + itr[5 * 10 ** n] * f + itr[1 * 10 ** n] * e
            return res

        itr = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }
        itr_2 = {
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM',
        }
        result: str = ''
        string_num: str = str(num)
        if len(string_num) == 4:
            result = itr[1000] * int(string_num[0])
            string_num = string_num[1:]
        if len(string_num) in [3, 4]:
            result = add_to_result(result, string_num[0], 2)
            result = add_to_result(result, string_num[1], 1)
            result = add_to_result(result, string_num[2], 0)
        if len(string_num) == 2:
            result = add_to_result(result, string_num[0], 1)
            result = add_to_result(result, string_num[1], 0)
        if len(string_num) == 1:
            result = add_to_result(result, string_num[0], 0)
        return result


print(Solution().intToRoman(3998))
