class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        # Make the preMap hashmap
        preMap = {i:[] for i in range(numCourses)}
        for course, preReq in prerequisites:
            if course not in preMap:
                preMap[course] = []
            preMap[course].append(preReq)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            
            if preMap[crs] == []:
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            preMap[crs] = []
            return True

        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

        
        

        