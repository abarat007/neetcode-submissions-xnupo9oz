class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # if nums total cant be divided evenly by k, we can't break it into equal subsets
        total = sum(nums)

        if total % k != 0:
            return False
        
        target = total // k

        nums.sort(reverse = True)

        if nums[0] > target:
            return False

        buckets = [0] * k

        def backtrack(idx):
            if idx == len(nums):
                return True
            
            num = nums[idx]

            for i in range(k):
                if buckets[i] + num <= target:
                    buckets[i] += num
                    
                    if backtrack(idx+1):
                        return True
            
                    buckets[i] -= num
            
                if buckets[i] == 0:
                    break
            
            return False
            
        
        return backtrack(0)


        