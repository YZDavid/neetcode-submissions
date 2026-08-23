class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")" : "(", "}" : "{", "]" : "["}
        for char in s:
            if char in pairs:
                opposing_pair = pairs[char]
                if not stack or opposing_pair != stack.pop():
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        return True


