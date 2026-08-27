class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # With n pairs of parentheses, you have available to you:
        # n opening parentheses [ ( ]
        # n closing parentheses [ ) ]


        res = []
        stack = []

        def backtrack(openCt, closedCt):
            # If we have finished building the string, add it to res
            if openCt == closedCt == n:
                res.append(''.join(stack))
                return
            
            if openCt < n:
                stack.append('(')
                backtrack(openCt+1, closedCt)
                stack.pop()

            
            if closedCt < n and closedCt < openCt:
                stack.append(')')
                backtrack(openCt, closedCt + 1)
                stack.pop()
        
        backtrack(0,0)
        return res



        