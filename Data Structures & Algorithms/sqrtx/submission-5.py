class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = 0
        while left <= right:
            mid = left + (right - left) // 2 #1
            if mid * mid > x:
                right = mid - 1 # 3
            if mid * mid < x:
                left = mid + 1
                res = mid
            if mid * mid == x:
                return mid
        
        return res
        


