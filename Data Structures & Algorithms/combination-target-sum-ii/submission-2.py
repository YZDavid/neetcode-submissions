class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index, remainder, choice):
            if remainder == 0:
                result.append(choice[:])
                return
            if remainder < 0:
                return
            if index == len(candidates):
                return
            # Choose
            choice.append(candidates[index])
            backtrack(index + 1, remainder - candidates[index], choice)
            choice.pop()

            # Do not choose
            while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, remainder, choice)
        
        backtrack(0, target, [])
        return result
                