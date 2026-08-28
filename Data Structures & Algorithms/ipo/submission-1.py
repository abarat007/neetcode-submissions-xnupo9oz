class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # profits = [1,4,2,3]
        # capital = [0,3,1,1]
        cap_to_profits = {}

        for c, p in zip(capital, profits):
            if c not in cap_to_profits:
                cap_to_profits[c] = []
            cap_to_profits[c].append(p)
        # {0: [1], 3: [4], 1: [2, 3]}
        
        capital_copy = list(cap_to_profits.keys()) # [0, 3, 1]
        heapq.heapify(capital_copy)
        
        maxCapital = [] # []

        # {0: [1], 3: [4], 1: [2, 3]}
        
        for _ in range(k):
            while capital_copy and capital_copy[0] <= w:
                curr_cap = heapq.heappop(capital_copy)
            
                for profit in cap_to_profits[curr_cap]:
                    heapq.heappush_max(maxCapital, profit)
            
            if not maxCapital:
                break
            
            best_profit = heapq.heappop_max(maxCapital)

            w += best_profit
        
        return w
            


        
        
        
            
                
