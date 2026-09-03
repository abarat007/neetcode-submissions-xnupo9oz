class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        endings = ")}]"

        for c in s:
            if c not in endings:
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0



        