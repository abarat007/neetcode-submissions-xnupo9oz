class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = -1
        left = 0
        right = n - 1

        # nums = [3,4,5,6,1,2], target = 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                res = mid
                break
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return res

        
        