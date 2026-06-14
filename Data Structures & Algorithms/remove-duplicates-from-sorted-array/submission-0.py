class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # non-decreasing order
        # I compare the current index value with the value to the right
        # If the current indexvalue to the right is == to the current index value, 
        # I remove the current index value and move the current index pointer by 1 to the right

        # nums = [1,2,2,3,4]
        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums [right - 1]:
                nums[left] = nums[right]
                left += 1
        
        return left


                
                






        