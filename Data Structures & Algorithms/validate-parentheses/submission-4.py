class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = list()
        for char in s:
            if char not in mapping:
                stack.append(char)
                continue
            if len(stack) == 0:
                return False
            pop = stack.pop(-1)
            if pop != mapping.get(char):
                return False
        if len(stack) > 0:
            return False
        return True
                