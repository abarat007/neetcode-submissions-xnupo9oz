class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # base case
        if n == 2:
            return [0,1]

        nums_map = {value:index for index, value in enumerate(nums)}
        # {3:0, 4:1, 5:2, 6:3}
        # nums = [3,4,5,6], target = 7
        # [5,5], target = 10
        for index, num in enumerate(nums):
            difference = target - num
            if difference in nums_map and nums_map[difference] != index:
                return [index, nums_map[difference]]




            
        

        