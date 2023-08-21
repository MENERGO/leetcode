class Solution:
    def countSegments(self, s: str) -> int:
        list_s = s.split(' ')
        list_new = [x for x in list_s if x != '']
        return len(list_new)
