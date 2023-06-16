class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        def create_dict(s):
            dict_s = {}
            for i in s:
                if i in dict_s:
                    dict_s[i] += 1
                else:
                    dict_s[i] = 1
            return dict_s

        return [k for k, v in create_dict(nums).items() if v == 1]
