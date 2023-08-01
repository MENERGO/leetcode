class Solution:
    def toHex(self, num: int) -> str:
        d = {
            '1111': 'f',
            '1110': 'e',
            '1101': 'd',
            "1100": 'c',
            "1011": 'b',
            "1010": 'a',
            "1001": '9',
            "1000": '8',
            "0111": '7',
            "0110": '6',
            '0101': '5',
            "0100": '4',
            "0011": '3',
            "0010": '2',
            "0001": '1',
            '0000': '0',
        }
        ddd = {
            0: '0',
            1: '1',
        }
        dd = {
            '0': '1',
            '1': '0',
        }
        prt = ''
        result = ''
        if num == 0:
            return '0'
        if num == -2147483648:
            return '80000000'
        if num > 0:
            while True:
                prt += "0123456789abcdef"[num % 16]
                num //= 16
                if num == 0:
                    return prt[::-1]
        else:
            num = abs(num)
            while True:
                if num >= 2:
                    prt += ddd[num % 2]
                    num = num // 2
                else:
                    prt += ddd[num]
                    if len(prt) < 32:
                        prt = '0' * (32 - len(prt)) + prt[::-1]
                    prt = ''.join([dd[x] for x in prt])
                    res_2 = ''
                    res_list = list(prt)[::-1]
                    k = True
                    for n, i in enumerate(res_list):
                        if k:
                            if i == '1':
                                res_2 += '0'
                            else:
                                res_2 += '1'
                                k = 0
                        else:
                            res_2 += ''.join(res_list[n:])
                            prt = res_2[::-1]
                            break
                    for i in range(0, 32, 4):
                        result += d[prt[i:i + 4]]
                    return result


'''
    def toHex(self, num):
        if num == 0:
            return '0'
        mp = '0123456789abcdef'  # like a map
        ans = ''
        for i in range(8):
            n = num & 15  # this means num & 1111b
            c = mp[n]  # get the hex char
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')  # strip leading zeroes
'''
