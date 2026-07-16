class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = {val:0 for val in range(1, n + 1)}
        outgoing = {val:0 for val in range(1, n + 1)}

        for OUT, IN in trust:
            incoming[IN] += 1
            outgoing[OUT] += 1
        
        for key in incoming:
            if incoming[key] == n-1 and outgoing[key] == 0:
                return key
        
        return -1
            

        














        
        