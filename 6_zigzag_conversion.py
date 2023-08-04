class Solution:
    def convert(self, s: str, numRows: int) -> str:
        import numpy as np
        n = numRows
        k = 0
        w = 0
        ns = ''
        for i in s:
            if k < n:
                ns += i
                k += 1
            else:
                if w < n - 1:
                    w += 1
                    ns += ' ' * (n - 2) + i
                else:
                    w = 0
                    k = 2
                    ns += i
        ns += ' ' * (n - len(ns) % n)
        arr = np.array(list(ns)).reshape(-1, n)
        return ''.join(arr.T.flatten()).replace(' ', '')


'''
        if len(s) <= numRows or numRows == 1:
            return s
        result = [''] * numRows
        rownumber = 0
        for i in s:
            if rownumber == 0:
                step = 1
            if rownumber == numRows - 1:
                step = -1
            result[rownumber] += i
            rownumber = rownumber + step
        return ''.join(result)
'''
