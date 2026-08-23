class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        characters = dict()
        for char in s1:
            if char not in characters:
                characters[char] = 0
            characters[char] += 1
        
        def check_characters():
            # Checks if all counts in characters is 0
            for count in characters.values():
                if count != 0:
                    return False
            return True
        
        # Init sliding window starting at index 0
        for i in range(len(s1)):
            char = s2[i]
            if char not in characters:
                characters[char] = 0
            characters[char] -= 1
        if check_characters():
            return True
        
        for i in range(len(s2)-len(s1)):
            left_char = s2[i]
            right_char = s2[i+len(s1)]
            if left_char not in characters:
                characters[left_char] = 0
            if right_char not in characters:
                characters[right_char] = 0
            characters[left_char] += 1
            characters[right_char] -= 1
            if check_characters():
                return True
        return False

            
