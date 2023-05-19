class Solution:
    def simplifyPath(self, path: str) -> str:
        if path[-1] != '/':
            path += '/'
        while '//' in path or '/./' in path:
            path = path.replace('//', '/')
            path = path.replace('/./', '/')
        if '/../' in path:
            count_dots = path.count('..')
            for i in range(count_dots):
                list_i = path.split('/')
                if list_i[0] == '':
                    list_i = list_i[1:]
                if list_i[-1] == '':
                    list_i = list_i[:-1]
                if list_i[0] != '..':
                    for n in range(len(list_i)):
                        if list_i[n] == '..':
                            list_i = list_i[:n - 1] + list_i[n + 1:]
                            break
                    path = '/' + '/'.join(list_i)
                else:
                    list_i = list_i[1:]
                    path = '/' + '/'.join(list_i)
        path = path.rstrip('/')
        if path == '':
            return '/'
        return path


'''
        path = path.split("/")
        res = []
        count = 0
        for i in path:
            if len(i) == 0 or i == ".":
                pass
            elif i == "..":
                if count:
                    res.pop()
                    count -= 1
            else:
                res.append(i)
                count += 1
        return ("/" + "/".join(res))
'''

print(Solution().simplifyPath("/AagbK/////iavh/M/rmKaS/tXD/././lND//"))
