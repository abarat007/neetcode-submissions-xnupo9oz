class Solution:
    def climbStairs(self, n: int) -> int:
        res = []
        res.append(1)
        res.append(1)
        left = 0
        right = 1

        for i in range(2,n+1):
            res.append(res[left]+res[right])
            left+=1
            right+=1

        return res[-1]
        