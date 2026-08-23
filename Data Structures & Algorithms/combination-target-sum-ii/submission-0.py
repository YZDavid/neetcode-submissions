class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        def generate(index, target, generated_lst):
            if target == 0:
                output.append(generated_lst.copy())
                return
            if target < 0:
                return
            if index == len(candidates):
                return

            # Choose this candidate
            chosen = candidates[index]
            remaining = target - chosen
            generated_lst.append(chosen)
            generate(index + 1, remaining, generated_lst)

            # Skip this candidate
            generated_lst.pop()
            # If we choose to skip this candidate, we need to skip all other similar candidates
            next_index = index + 1
            while next_index < len(candidates):
                if candidates[index] != candidates[next_index]:
                    break
                index += 1
                next_index += 1
            generate(index + 1, target, generated_lst)
        
        generate(0, target, [])
        return output