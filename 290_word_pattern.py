class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(' ')
        if len(pattern) != len(list_s):
            return False
        d = {}
        for i in range(len(list_s)):
            if list_s[i] not in d.values():
                d[pattern[i]] = list_s[i]
        new_list = []
        for i in pattern:
            if i not in d.keys():
                return False
            new_list.append(d[i])
        return s == ' '.join(new_list)


print(Solution().wordPattern(pattern="abba", s="dog dog dog dog"))
