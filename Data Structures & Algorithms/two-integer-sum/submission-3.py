class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_list = []
        # 1. We should store the nums indices and its values as num:idx pairs in a dictionary
        nums_dict = {}

        # 2. We can loop through the nums list and see if the map has the difference value. If not, we add it to the dict and continue
        for idx, value in enumerate(nums):
            difference = target - value
            if difference in nums_dict:
                return [nums_dict[difference], idx]
            nums_dict[value] = idx
        
        # 3. Sort the return list and return
        return_list_sorted = sort(return_list)
        return return_list_sorted




        