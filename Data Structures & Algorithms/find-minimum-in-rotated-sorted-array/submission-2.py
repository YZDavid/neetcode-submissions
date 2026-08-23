class Solution:
    def findMin(self, nums: List[int]) -> int:
        def condition(idx):
            return nums[idx] < nums[0]
        
        def binary_search(nums):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                print(l, m, r)
                if condition(m):
                    r = m
                else:
                    l = m + 1
            return l

        con_arr = [condition(i) for i in range(len(nums))]
        print(con_arr)

        # Run binary search and see the index it ends up on
        idx = binary_search(nums)
        print(idx)

        # If this index has a conditional of False, we know that
        # the search could not find any rotated value. Therefore,
        # we should return the first item in the array
        con = condition(idx)
        print(con)
        if not con:
            return nums[0]
        # Otherwise, this is the rotated value
        return nums[idx]
