class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by the first value of each interval
        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]

        for start_time, end_time in intervals[1:]:
            # if they don't overlap
            if start_time > res[-1][1]:
                res.append([start_time, end_time])
            else: # the interval overlap
                res[-1][1] = max(res[-1][1], end_time)
        return res
                
            

        