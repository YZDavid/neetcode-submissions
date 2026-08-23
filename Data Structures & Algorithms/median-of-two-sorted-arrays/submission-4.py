class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        combined_len = (len(nums1) + len(nums2))
        # Using + 1 makes the left half larger for odd lengths.
        # Example: len 5 -> left gets 3, right gets 2.
        target_combined_len = (combined_len + 1) // 2 
        l, r = 0, len(A)

        def condition(elemsA):
            elemsB = target_combined_len - elemsA
            
            # Using your excellent boundary logic
            leftA = float("-inf") if elemsA == 0 else A[elemsA - 1]
            leftB = float("-inf") if elemsB == 0 else B[elemsB - 1]
            rightA = float("inf") if elemsA == len(A) else A[elemsA]
            rightB = float("inf") if elemsB == len(B) else B[elemsB]
            
            # THE FIX: We only check if A is too far to the right.
            # This restores our [F, F, T, T] monotonicity!
            return rightA >= leftB

        def condition_(mid_A) -> bool:
            mid_B = target_combined_len - mid_A
            
            # Boundary values (handle out-of-bounds with infinity)
            R1 = A[mid_A] if mid_A < len(A) else float('inf')
            L2 = B[mid_B - 1] if mid_B > 0 else float('-inf')
            
            # The monotonic question: Is our cut in A far enough to the right 
            # that its right element can cover B's left element?
            return R1 >= L2

        while l < r:
            m = l + (r - l) // 2 # Avoids integer overflow (best practice)
            
            if condition(m):
                # leftA > rightB. A has too many elements. Move left.
                r = m 
            else:
                # We are either perfect, or A needs more elements. Move right.
                l = m + 1
        
        # Post-Processing
        lenA = l
        lenB = target_combined_len - lenA
        
        # Keep using infinities to avoid NoneType comparison errors
        leftA = float("-inf") if lenA == 0 else A[lenA - 1]
        rightA = float("inf") if lenA == len(A) else A[lenA]
        leftB = float("-inf") if lenB == 0 else B[lenB - 1]
        rightB = float("inf") if lenB == len(B) else B[lenB]
        
        # In an odd case, median is the max of the left side (since left is bigger)
        if combined_len % 2 == 1:
            return float(max(leftA, leftB))
            
        # In an even case, average of max left and min right
        return (max(leftA, leftB) + min(rightA, rightB)) / 2.0