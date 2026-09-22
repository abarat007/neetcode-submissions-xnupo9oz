class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # we ignore all negative values
        # We know that the answer has to lie between 1 and n inclusive
        # if it doesnt, then the answer has to be n+1

        # We want in the array each index to have value of index + 1
        # For example: 
        # if nums = [1,2,4]

        # idx  val
        #  0   1
        #  1   2
        #  2   3
        
        # I am going to loop through range(n)
        for i in range(n):
            # if it's positive and value != idx + 1 and the value is in range, swap
            while n >= nums[i] >= 1 and nums[nums[i]-1] != nums[i]:
                swapping_idx = nums[i] - 1
                # swap
                nums[i], nums[swapping_idx] = nums[swapping_idx], nums[i]
        
        # Loop through nums. The first instance where nums[i] != i + 1, we return that value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If that runs without returning anything, then all the numbers are in place
        # so the answer is n+1
        return n + 1


                
        




        