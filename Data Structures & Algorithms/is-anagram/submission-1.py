class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for char in s:
            d[char] = d.get(char, 0) + 1
        for char in t:
            d[char] = d.get(char, 0) - 1
        for char, count in d.items():
            if count != 0:
                return False
        return True
    