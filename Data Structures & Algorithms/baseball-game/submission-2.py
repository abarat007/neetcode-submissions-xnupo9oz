class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:           
            if val == "+":
                stack.append(stack[-1] + stack[-2])
            elif val == "C":
                stack.pop()
            elif val == "D":
                doubled_score = stack[-1] * 2
                stack.append(doubled_score)
            else:
                stack.append(int(val))
        
        total = sum(stack)
        return total

        