class Solution:
    def isValid(self, s: str) -> bool:
        s_stack = []
        endings = '}])'

        if len(s) == 1:
            return False

        for letter in s:
            if letter not in endings:
                s_stack.append(letter)
            else:
                if not s_stack:
                    return False

                if letter == '}' and s_stack[-1] == '{':
                    s_stack.pop()
                elif letter == ']' and s_stack[-1] == '[':
                    s_stack.pop()
                elif letter == ')' and s_stack[-1] == '(':
                    s_stack.pop()
                else:
                    return False

        return len(s_stack) == 0

        