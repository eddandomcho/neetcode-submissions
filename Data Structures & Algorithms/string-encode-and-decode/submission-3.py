class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "Empty"
        final_string = ""
        for i in range(len(strs)):
            final_string += strs[i]
            if i == len(strs) - 1:
                break
            final_string += "[break]"
        return final_string
    def decode(self, s: str) -> List[str]:
        if s=="Empty":
            return []
        return s.split("[break]")