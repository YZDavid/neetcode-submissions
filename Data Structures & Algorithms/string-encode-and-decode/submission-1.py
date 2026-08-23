class Solution:

    def encode(self, strs: List[str]) -> str:
        # Need some sort of delimiter that tells us the length of the word and also
        # indicates that it is a delimiter
        encoded = ""
        for word in strs:
            delim = str(len(word)) + "$"
            encoded += delim + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        num_arr = []
        i = 0
        while i < len(s):
            char = s[i]
            if char.isnumeric():
                num_arr.append(char)
                i += 1
            elif char == "$":
                len_word = int("".join(num_arr))
                num_arr = []
                start_idx = i + 1
                end_idx = start_idx + len_word
                word = s[start_idx:end_idx]
                decoded.append(word)
                i = end_idx
            else:
                i += 1
        return decoded

