class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # base case
        if n == 1:
            return [0]
        
        res = [0] * n

        stack = [] # (temp, index)

        # [30,38,30,36,35,40,28]
        # (30,0) (38,1) (30,2) (36,3) (35,4) (40,5) (28,6)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = index - stack_idx
            stack.append((temp, index))
        
        return res


        






        
        


        