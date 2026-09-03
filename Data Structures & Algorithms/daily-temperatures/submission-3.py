class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # (temp, idx)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp, stack_idx = stack.pop()
                result[stack_idx] = idx - stack_idx
            stack.append((temp, idx))
        
        return result

            


        






            