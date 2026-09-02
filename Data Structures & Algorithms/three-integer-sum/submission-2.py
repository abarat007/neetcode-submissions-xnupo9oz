class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        target = 0
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            anchor = nums[i]
            complement_sum = target - anchor
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total == complement_sum:
                    triplet = [anchor, nums[left], nums[right]]
                    triplets.append(triplet)
                    left += 1
                    right -= 1
                elif total < complement_sum:
                    left += 1
                else:
                    right -= 1

        triplets_cleaned = [list(x) for x in set(tuple(i) for i in triplets)]
        return triplets_cleaned










        

        