class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        final_str = []
        # s = "2[a3[b]]c"
        # "abbbabbbc"

        # stack = ['2','[','a','3','[','b']

        for i in range(len(s)):
            # add to the stack if it's not ']'
            if s[i] != ']':
                stack.append(s[i])
            # if it is ']', then we build a temp substring by popping until we encounter '['
            if s[i] == ']':
                temp_str = ''
                while stack[-1] != '[':
                    temp_str = stack.pop() + temp_str
                    #stack = ['2','[','a','3','[']
                # remove the '['
                stack.pop() # stack = ['2','[','a','3'] 
                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier # 3
                temp_str *= int(multiplier)
                stack.append(temp_str) # stack = [2,[,a,bbb] 
        
        return ''.join(stack)
            
            



        