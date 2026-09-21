class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n # handles any k that is greater than n

        # nums = [1,2,3,4,5,6,7,8]  k = 4

        # # Step 1: Reverse nums
        # nums = [8,7,6,5,4,3,2,1]

        # # Since k = 4, from idx = 4 to idx = n-1, reverse those digits
        # nums = [8,7,6,5,1,2,3,4]

        # # Now we reverse digits from idx = 0 to idx = k-1
        # nums = [5,6,7,8,1,2,3,4]

        def reverse(left, right):
            while left < right:
                # swap left and right indices
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        
        reverse(0, n-1)
        reverse(k, n-1)
        reverse(0, k-1)


