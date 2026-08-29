class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        connectionMap = {i:[] for i in range(n)}
        for x,y in edges:
            connectionMap[x].append(y)
            connectionMap[y].append(x)
        
        visited = set()
    
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for connection in connectionMap[node]:
                if connection == parent:
                    continue
                if not dfs(connection, node):
                    return False
        
            return True
        
        if not dfs(0,-1):
            return False

        return len(visited) == n
        


        
