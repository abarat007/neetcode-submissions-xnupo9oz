class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        preMap = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            if course in preMap:
                preMap[course].append(prereq)
            else:
                preMap[course] = []
                preMap[course].append(prereq)
        
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
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

        
        

        