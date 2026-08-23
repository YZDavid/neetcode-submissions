class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        prev_output = [[]]
        for digit in digits:
            letters = mapping[int(digit)]
            curr_output = []
            for letter in letters:
                for comb in prev_output:
                    curr_arr = comb.copy()
                    curr_arr.append(letter)
                    curr_output.append(curr_arr)
            prev_output = curr_output
        if len(prev_output[0]) == 0:
            return []
        return list(map(lambda x: "".join(x), prev_output))

        