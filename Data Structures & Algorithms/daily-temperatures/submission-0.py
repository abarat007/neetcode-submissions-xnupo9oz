class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # base case
        if len(temperatures) == 1:
            return [0]
        
        res = [0] * n
        stack = [] # (temp, index)
        
        # [30,38,30,36,35,40,28]

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = index - stack_index
            stack.append((temp, index))
        
        return res

        






        
        


        