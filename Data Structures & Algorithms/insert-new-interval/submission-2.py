class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Edge Case 1: if newInterval[1] < intervals[0][0], then add newInterval to the front of intervals

        # Edge Case 2: if newInterval[0] > intervals[-1][1], then append newInterval to intervals

        # newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res = []
        for i in range(len(intervals)):
            # Edge Case 1:
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            # Edge Case 2:
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [(min(newInterval[0], intervals[i][0])), (max(newInterval[1], intervals[i][1]))]
                
        res.append(newInterval)
        return res

        
    



        
        