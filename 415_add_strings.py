class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        eq = {
            '00': '0',
            '19': '10',
            '28': '10',
            '37': '10',
            '46': '10',
            '55': '10',
            '01': '1',
            '29': '11',
            '38': '11',
            '47': '11',
            '56': '11',
            '02': '2',
            '11': '2',
            '39': '12',
            '48': '12',
            '57': '12',
            '66': '12',
            '03': '3',
            '12': '3',
            '49': '13',
            '58': '13',
            '67': '13',
            '04': '4',
            '13': '4',
            '22': '4',
            '59': '14',
            '68': '14',
            '77': '14',
            '05': '5',
            '14': '5',
            '23': '5',
            '69': '15',
            '78': '15',
            '06': '6',
            '15': '6',
            '24': '6',
            '33': '6',
            '79': '16',
            '88': '16',
            '07': '7',
            '16': '7',
            '25': '7',
            '34': '7',
            '89': '17',
            '08': '8',
            '17': '8',
            '26': '8',
            '35': '8',
            '44': '8',
            '99': '18',
            '09': '9',
            '18': '9',
            '27': '9',
            '36': '9',
            '45': '9',
        }

        def add_my(a, b):
            plus_one = '0'
            if a > b:
                a, b = b, a
            x1 = eq[a + b]
            if len(x1) == 2:
                x = x1[1]
                plus_one = '1'
            else:
                x = x1
            return x, plus_one

        result = ''
        rank = '0'
        rank2 = '0'

        if len(num1) > len(num2):
            num1, num2 = num2, num1
        num1 = '0' * (len(num2) - len(num1) + 1) + num1
        num2 = '0' + num2

        for i in range(1, len(num1) + 1):
            n1, n2 = num1[-i], num2[-i]
            if rank != '0':
                if n1 > rank:
                    n1, rank = rank, n1
                n1, rank2 = add_my(n1, rank)
            num, rank = add_my(n1, n2)
            if rank == '1' and rank2 == '1':
                rank = '2'
            if rank == '0' and rank2 == '1':
                rank = '1'
            result += num
        result = result[::-1]
        if result[0] == '0':
            result = result[1:]
        return result
