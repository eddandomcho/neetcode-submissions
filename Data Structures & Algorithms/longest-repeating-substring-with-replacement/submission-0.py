class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = -1
        
        charSet = set(s)
        for c in charSet:
            replaced = k
            left = 0
            for right in range(len(s)):
                if s[right] != c:
                    replaced -= 1
                    
                while replaced < 0:
                    if s[left] != c:
                        replaced += 1
                    left +=1
                
                max_len = max(right - left + 1, max_len)
        return max_len



