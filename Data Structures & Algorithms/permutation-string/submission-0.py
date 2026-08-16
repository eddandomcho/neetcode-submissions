class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        for right in range(k, len(s2) + 1):
            substring = s2[right - k : right]
            if sorted(substring) == sorted(s1):
                return True
        return False