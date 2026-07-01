class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips.sort(key = lambda x: x[1])
        location_changes = {} # {location: net passenger change}

        # trips = [[2,1,3],[3,2,4]] # trips = [[4,1,2],[3,2,4]]
        for i in range(len(trips)):
            location_changes[trips[i][1]] = location_changes.get(trips[i][1], 0) + trips[i][0]
            location_changes[trips[i][2]] = location_changes.get(trips[i][2], 0) - trips[i][0]
        
        curr_passenger = 0
        sorted_location_changes = dict(sorted(location_changes.items()))
        # print(f'Sorted dictionary: {sorted_location_changes}')
        for loc in sorted_location_changes:
            curr_passenger += sorted_location_changes[loc]

            if curr_passenger > capacity:
                return False
        
        return True


            
            

                
        






