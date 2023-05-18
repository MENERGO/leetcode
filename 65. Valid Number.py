class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        if s == '-' or s == '+' or s == '.' or s == 'e':
            return False
        if '--' in s or '++' in s or '-+' in s or '+-' in s:
            return False
        if s.count('-') > 2 or s.count('+') > 2 or s.count('.') > 1 or s.count('e') > 1:
            return False
        if s[0] == '-':
            s = s.lstrip('-')
        if s[0] == '+':
            s = s.lstrip('+')
        alf = 'qwrtyuioplkjhgfdsazxcvbnm'
        if len(set(s) & set(alf)) > 0:
            return False
        if 'e' in s:
            f, l = s.split('e')
            if len(f) == 0 or len(l) == 0 or '.' in l:
                return False
            if len(l) == 1 and ('.' in l or '+' in l or '-' in l):
                return False
            if l[0] == '-':
                l = l.lstrip('-')
            if l[0] == '+':
                l = l.lstrip('+')
            if '+' in l or '-' in l or '+' in f or '-' in f:
                return False
            f = f.replace('.', '')
            if f.isdigit() and l.isdigit():
                return True
            return False
        if '.' in s:
            if '+' in s or '-' in s:
                return False
            f, l = s.split('.')
            if f.isdigit() and l.isdigit():
                return True
            if f.isdigit() and len(l) == 0:
                return True
            if len(f) == 0 and l.isdigit():
                return True
            return False
        if s.isdigit():
            return True
        return False


'''
        if 'inf' in str.lower(s):
            return False
        try:
            key=float(s)
            return True
        except:
            return False
'''

'''
        try: float(s)
        except: return False
        return "inf" not in s.lower()
'''

print(Solution().isNumber('abc'))
