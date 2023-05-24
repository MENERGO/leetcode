class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        s = re.sub(r"[ ,.:;!?@$#%^&*()_\-\+=\\|\"'\?`~№\[\]\{\}]", '', s)
        return s == s[::-1]
