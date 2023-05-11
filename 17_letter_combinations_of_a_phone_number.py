class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        d: dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        if digits == '':
            return []
        result: list = []
        if len(digits) == 1:
            return [i for i in d[digits[0]]]
        first: list = self.letterCombinations(digits[1:])
        for f in first:
            for i in d[digits[0]]:
                result.append(i + f)
        return result


print(Solution().letterCombinations(digits='23'))

'''
        dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if digits == "": # blank case
            return []
        chars=[]
        for c in digits:
            chars.append(dict[c])
        code = product(*chars)
        #The product() function from the itertools module generates the cartesian product of the input iterables.
        lst = []
        for k in code:
            lst.append(''.join(k))
        return lst
'''

'''
        if not digits:
            return []
        keypad = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
                }
        b = [keypad[i] for i in digits]
        return list(map(''.join, product(*b)))
'''
