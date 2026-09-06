class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if len(intervals) == 1:
            return 0
        n = len(intervals)
        intervals.sort(key = lambda x: x[0])
        # print(intervals)
        res = [intervals[0]]
        removals = 0

        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            # if there's no overlap, then append to res
            if curr_start >= res[-1][1]:
                res.append(intervals[i])
            else: # there is overlap
                removals += 1
                res[-1][1] = min(res[-1][1], curr_end)

        
        return removals


        