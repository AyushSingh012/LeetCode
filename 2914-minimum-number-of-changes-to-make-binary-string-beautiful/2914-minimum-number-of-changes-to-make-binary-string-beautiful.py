class Solution:
    def minChanges(self, s: str) -> int:
        return (int(s[::2], 2) ^ int(s[1::2], 2)).bit_count()
        