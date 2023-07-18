class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in magazine:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in set(ransomNote):
            if i in d:
                if ransomNote.count(i) > d[i]:
                    return False
            else:
                return False
        return True


'''

        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
        
'''
