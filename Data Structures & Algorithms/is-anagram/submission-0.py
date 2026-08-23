class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_counts = [0] * 26
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            idx_s = ord(char_s) % 97
            idx_t = ord(char_t) % 97
            char_counts[idx_s] += 1
            char_counts[idx_t] -= 1
        
        for count in char_counts:
            if count != 0:
                return False
        return True

        