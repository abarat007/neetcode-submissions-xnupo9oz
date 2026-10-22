class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mapping = defaultdict(list)

        for ticket in tickets:
            from_city, to_city = ticket[0], ticket[1]
            mapping[from_city].append(to_city)
        
        for val in mapping.values():
            val.sort(reverse = True)
        
        itinerary = []
        def dfs(city):
            while mapping[city]:
                dest = mapping[city].pop()
                dfs(dest)
            itinerary.append(city)
        
        dfs("JFK")
        return itinerary[::-1]







        