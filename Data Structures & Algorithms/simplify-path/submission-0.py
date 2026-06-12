class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []
        # print(paths)
        # ['', 'neetcode', 'practice', '', '...', '', '', '..', 'courses']
        for x in paths:
            if x == '' or x == '.':
                continue
            elif x == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
            
        
        return '/' + '/'.join(stack)


