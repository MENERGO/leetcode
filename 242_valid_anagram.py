class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def create_dict(s):
            dict_s = {}
            for i in s:
                if i in dict_s:
                    dict_s[i] += 1
                else:
                    dict_s[i] = 1
            return dict_s

        return create_dict(t) == create_dict(s)
