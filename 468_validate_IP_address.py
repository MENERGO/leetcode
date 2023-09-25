class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        import re
        if '.' in queryIP:
            list_q = queryIP.split('.')
            len_q = len(list_q)
            if len_q == 4:
                for i in list_q:
                    if i.isdigit() and str(int(i)) == i:
                        if int(i) < 0 or int(i) > 255:
                            return 'Neither'
                    else:
                        return 'Neither'
                return 'IPv4'
        elif ':' in queryIP:
            list_q = queryIP.split(':')
            len_q = len(list_q)
            if len_q == 8:
                for i in list_q:
                    if len(i) > 4 or len(i) < 1:
                        return 'Neither'
                    if not re.match(r'^[0-9A-Fa-f]{1,4}$', i):
                        return 'Neither'
                return 'IPv6'
        return 'Neither'
