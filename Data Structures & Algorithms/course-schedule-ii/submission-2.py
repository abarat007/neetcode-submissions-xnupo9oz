class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []

        # Build preMap
        preMap = {i:[] for i in range(numCourses)}
        for course, preReq in prerequisites:
            if course not in preMap:
                preMap[course] =[]
            preMap[course].append(preReq)
        
        visited = set()
        completed = set()
        def dfs(crs):
            if crs in visited:
                return False
            
            if crs in completed:
                return True
            
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            completed.add(crs)
            order.append(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return order
                
        
        