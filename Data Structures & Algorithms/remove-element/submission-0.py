class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        n = len(nums)

        while left < n:
            if nums[left] == val:
                n -= 1
                nums[left] = nums[n]
            else:
                left += 1
        return n

        

        
    
        
                
        

        