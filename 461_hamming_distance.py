class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x).lstrip('0b')
        y = bin(y).lstrip('0b')
        if len(x) < len(y):
            x, y = y, x
        y = '0' * (len(x) - len(y)) + y
        result = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                result += 1
        return result


'''

        return bin(x^y).count('1')

'''
