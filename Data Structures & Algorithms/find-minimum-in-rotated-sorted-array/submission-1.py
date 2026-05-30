class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        res = nums[0]

        # nums = [3,4,5,6,1,2]
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = left + (right - left) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return res



        