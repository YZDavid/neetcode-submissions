class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())
        left_ptr = 0
        right_ptr = len(s) - 1
        while left_ptr <= right_ptr:
            left_c = s[left_ptr]
            right_c = s[right_ptr]
            if left_c != right_c:
                return False
            left_ptr += 1
            right_ptr -= 1
        return True
            
            