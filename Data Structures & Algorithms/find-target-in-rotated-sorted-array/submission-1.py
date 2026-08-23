class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_rotated_index(nums):
            l, r = 0, len(nums) - 1
            min_val = 1000
            min_idx = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= nums[l]:
                    if nums[l] < min_val:
                        min_val = nums[l]
                        min_idx = l
                    l = mid + 1
                else:
                    if nums[mid] < min_val:
                        min_val = nums[mid]
                        min_idx = mid
                    r = mid - 1
            return min_idx
        
        def binary_search(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return -1
        
        min_idx = find_rotated_index(nums)
        smallest_num = nums[min_idx]

        last_num = nums[-1]
        if target <= last_num:
            res = binary_search(nums[min_idx:], target)
            print("case 1")
            print(res)
            if res == -1:
                return -1
            return min_idx + res
        else:
            res = binary_search(nums[:min_idx], target)
            print("case 2")
            print(res)
            if res == -1:
                return -1
            return res
        

