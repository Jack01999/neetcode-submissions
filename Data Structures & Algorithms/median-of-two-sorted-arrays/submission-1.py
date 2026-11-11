class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        # Make sure a is the smaller array
        if len(B) < len(A):
            A,B = B,A

        left,right = 0,len(A)-1
        mid, diff = 0,0
        while True:
            # Find left partition of A
            mid = (left + right) // 2
            # Find left partition of B
            # (mid+1 to account for A index)
            # (- 1 to account for B index)
            diff = half - (mid+1) - 1

            Aleft = A[mid] if mid >= 0 else float('-inf')
            Aright = A[mid+1] if (mid + 1) < len(A) else float('inf')
            Bleft = B[diff] if diff >= 0 else float('-inf')
            Bright = B[diff+1] if (diff + 1) < len(B) else float('inf')

            # Check if left partitions are valid
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft,Bleft) + min(Aright, Bright))/2
                else:
                    return min(Aright,Bright)
            elif Bleft > Aright:
                # A's Left partition is too small
                left = mid+1
            elif Aleft > Bright:
                # A's Left partition is too big
                right = mid-1


        