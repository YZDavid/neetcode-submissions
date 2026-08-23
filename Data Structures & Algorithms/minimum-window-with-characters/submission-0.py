class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base cases: If s or t are empty:
        if not s or not t:
            return ""
        
        # Count freq of chars in t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        # Num unique characters in freq count
        num_chars = len(t_count)
        
        # Sliding window
        left, right = 0, 0
        matching_chars = 0
        window_count = {}
        best = (1001, None, None)

        while right < len(s):
            right_char = s[right]
            window_count[right_char] = window_count.get(right_char, 0) + 1
            # If this newly added char is in the t_count and matches,
            if right_char in t_count and t_count[right_char] == window_count[right_char]:
                matching_chars += 1
            
            # If we end up with all matching chars, we try to contract the sliding window
            while left <= right and matching_chars == num_chars:
                left_char = s[left]
                # Check smallest window so far? Compare against curr best
                if right - left + 1 < best[0]:
                    best = (right - left + 1, left, right)
                # Update window_count
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    matching_chars -= 1
                    # This will break the internal while loop
                
                left += 1
            
            right += 1
        
        if best[0] == 1001:
            return ""
        return s[best[1]:best[2] + 1]

        