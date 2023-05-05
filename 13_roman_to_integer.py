class Solution:
    def romanToInt(self, s: str) -> int:
        rti: dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,

        }
        rti_2: dict = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,

        }
        result: int = 0
        for k, v in rti_2.items():
            if k in s:
                result += v
                s = s.replace(k, '')
        for i in s:
            result += rti[i]
        return result


print(Solution().romanToInt(s=""))
