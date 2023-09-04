class Solution:
    def frequencySort(self, s: str) -> str:
        dict_s = {}
        result = ''
        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1
        dict_s = {k: v for k, v in sorted(dict_s.items(), key=lambda item: item[1], reverse=True)}
        for k, v in dict_s.items():
            for i in range(v):
                result += k
        return result
