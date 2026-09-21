class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val:idx
        n = len(nums)
        for i in range(n):
            difference = target - nums[i]
            if difference in seen:
                return [seen[difference], i]
            seen[nums[i]] = i

        