class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = [0] * len(queries)
        graph = {}

        for i in range(len(equations)):
            numerator = equations[i][0]
            denominator = equations[i][1]
            val = values[i]

            if numerator not in graph:
                graph[numerator] = []
            if denominator not in graph:
                graph[denominator] = []
            
            graph[numerator].append((denominator, val))
            graph[denominator].append((numerator, float(1/val)))
        
        
        def dfs(curr, target, product, visited):
            if curr == target:
                return product
            
            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, product * weight, visited)
                    if result != -1.0:
                        return result
            
            return -1.0



        # queries = [["a","c"],["b","a"],["c","c"],["ab","a"],["d","d"]]

        # graph:
        # 'a': [('b', 4.0)]
        # 'b': [('a', 0.25), ('c', 1.0)]
        # 'c': [('b', 1.0)]
        # 'ab': [('bc', 3.25)]
        # 'bc': [('ab', 0.3076923076923077)]




        for i in range(len(queries)):
            numerator = queries[i][0]
            denominator = queries[i][1]
            # we gotta find a path from the numerator and denominator
            # if num/den not in the graph, set it as -1.0
            if numerator not in graph or denominator not in graph:
                res[i] = -1.0
            else:
                # dfs through the graph and build the answer
                visited = set()
                answer = dfs(numerator, denominator, 1.0, visited)
                res[i] = answer
        
        return res



        







        