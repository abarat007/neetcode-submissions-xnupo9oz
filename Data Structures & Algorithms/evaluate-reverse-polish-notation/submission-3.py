class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        stack = []
        symbols_str = '+-*/'
        if (len(tokens) == 1) and (tokens[0] not in symbols_str):
            stack.append(tokens[0])
            return int(tokens[0])
        
        number_counter = 0
        
        # [1,2]
        for token in tokens:
            if token not in symbols_str:
                stack.append(token)
            else:
                first = stack.pop() # '2'
                second = stack.pop() # '1'
                expression_str = f'{second} {token} {first}'
                temp_res = int(eval(expression_str))
                stack.append(temp_res)
                result += temp_res
        
        return stack[0]
                




        

        