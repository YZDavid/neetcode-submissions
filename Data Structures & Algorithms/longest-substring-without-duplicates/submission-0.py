class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_chars = set()
        longest_substring = 0
        length = 0
        l, r = 0, 0
        while r < len(s):
            char = s[r]
            length += 1
            if char in curr_chars:
                while l < r:
                    left_char = s[l]
                    l += 1
                    length -= 1
                    if left_char == char:
                        break
                    curr_chars.remove(left_char)
    
            curr_chars.add(char)
            longest_substring = max(longest_substring, length)
            r += 1
        
        return longest_substring

