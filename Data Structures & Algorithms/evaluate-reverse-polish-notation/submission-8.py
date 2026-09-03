class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = "+-*/"
        res = 0

        for token in tokens:
            if token not in symbols:
                stack.append(int(token))
            elif token in symbols:
                second = stack.pop() # 2
                first = stack.pop() # 1
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))

        return stack[-1]

            
        
                




        

        