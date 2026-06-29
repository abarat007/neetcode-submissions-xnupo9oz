class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasks[i] = [enqueueTime, processingTime]
        # If CPU idle and tasks are available, we choose the task with
        # the shortest processingTime

        # We will need to use a min heap to accurately pop tasks based on processingTime
        # In min heap, we store each task as (processingTime, index)
        # Sort tasks by enqueueTime

        # tasks = [[1,4],[3,3],[2,1]]
        tasks_indexed = [(task[0],task[1], idx) for idx, task in enumerate(tasks)]
        
        tasks_indexed.sort(key = lambda x: x[0]) # (enqueueTime, processingTime, index)
        # [(1, 4, 0), (2, 1, 2), (3, 3, 1)]

        min_heap = [] # (processingTime, index)
        res = []
        time = 0
        i = 0

        while i < len(tasks_indexed) or min_heap:
            if not min_heap and time < tasks_indexed[i][0]:
                time = tasks_indexed[i][0]
            while i < len(tasks_indexed) and tasks_indexed[i][0] <= time:
                enqueueTime, processTime, index = tasks_indexed[i]
                heapq.heappush(min_heap, (processTime, index))
                i += 1
            processTime, idx = heapq.heappop(min_heap)
            res.append(idx)
            time += processTime
        
        return res
            


        



        
   




    



    