class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = False

        nums_map = {}

        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                isDuplicate = True
                break
        
        return isDuplicate
        