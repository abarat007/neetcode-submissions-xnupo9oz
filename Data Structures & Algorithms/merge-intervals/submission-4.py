class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # We should sort intervals by the first value of each interval
        intervals.sort(key = lambda x: x[0])
        

        
        # If the second interval starts after the previous one ends, its not overlapping
        # Otherwise, the intervals are overlapping

        # Iterate through the intervals list
        # If they don't overlap, we append it to res

        # If they do overlap, then we extend the existing interval in res: res[-1][1] = max(intervas[i][1], res[-1][1]) 

        res = [intervals[0]] # [[1,5]]
        for i in range (1, len(intervals)): # [6,7]
            # Edge Case 1: The intervals don't overlap
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else: # The intervals overlap
                res[-1][1] = max(intervals[i][1], res[-1][1])
            
        return res
            

        