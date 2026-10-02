class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        count = 0

        if '0000' in deadends:
            return -1
        
        queue = deque()
        queue.append(['0000', 0]) # lock state, # of turns
        visited = set(deadends)
        
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res


        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append([child, turns + 1])
        
        return -1






        






        


        