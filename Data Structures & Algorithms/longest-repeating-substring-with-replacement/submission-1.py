class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_substring = 0
        char_array = [0] * 26
        window = []
        l, r = 0, 0
        while r < len(s):
            # Add r index character to window
            char = s[r]
            window.append(char)
            # Keep track of count of character
            char_idx = ord(char) % 65
            char_array[char_idx] += 1
            # Check if window is valid
            conversions = len(window) - max(char_array)
            print(window)
            if conversions <= k:
                # If valid, update longest window
                longest_substring = max(longest_substring, len(window))
                print(f"IF TRUE conversions: {conversions}, r: {r}")
            else:
                # If not valid, remove leftmost char until valid
                while conversions > k:
                    removed_char = window.pop(0)
                    removed_idx = ord(removed_char) % 65
                    char_array[removed_idx] -= 1
                    conversions = len(window) - max(char_array)
            r += 1
        return longest_substring




            
