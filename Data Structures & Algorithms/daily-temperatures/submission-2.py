class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return [0]
        
        res_list = [0] * len(temperatures) 

        stack = [] 

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp, stack_index = stack.pop()
                res_list[stack_index] = idx - stack_index
            stack.append((temp, idx))

        return res_list 


        






            