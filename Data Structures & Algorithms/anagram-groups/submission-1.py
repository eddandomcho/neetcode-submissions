class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        big_dict = dict()
        for word in strs:
            if "".join(sorted(word)) not in big_dict:
                big_dict["".join(sorted(word))] = [word]
                continue
            big_dict["".join(sorted(word))].append(word)
        return list(big_dict.values())
