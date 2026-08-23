class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        def backtrack(idx, remainder, curr):
            if remainder < 0:
                return
            if remainder == 0:
                output.append(curr[:])
                return
            if idx == len(candidates):
                return
            # Choose
            curr.append(candidates[idx])
            backtrack(idx + 1, remainder - candidates[idx], curr)
            curr.pop()

            # Do not choose
            new_idx = idx
            while new_idx < len(candidates) - 1 and candidates[new_idx] == candidates[new_idx + 1]:
                new_idx += 1
            new_idx += 1
            backtrack(new_idx, remainder, curr)
        backtrack(0, target, [])
        return output