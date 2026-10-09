class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # [2,4,10,1,5]
        low = max(nums) # 10
        high = sum(nums) # 22
        res = high
        def can_split(mid):
            subarray = 1
            currSum = 0
            for num in nums:
                currSum += num
                if currSum > mid:
                    subarray += 1
                    if subarray > k:
                        return False
                    currSum = num
            return True

        
        while low <= high:
            mid = (low+high) // 2
            if can_split(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res
                




