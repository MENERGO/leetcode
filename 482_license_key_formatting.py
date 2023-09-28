class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        f = 0
        out = []
        for i in range(len(s) // k):
            out.append(s[f:i * k + k][::-1])
            f += k
        if f != len(s):
            out.append(s[f:][::-1])
        return '-'.join(reversed(out))
