class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            middle = (low + high) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                low += 1
            else:
                high -= 1
        
        return -1
        