class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Each boat has a weight limit of 'limit', and a person limit of 2
        # Each people[i] will be <= limit
        left = 0
        right = len(people) - 1
        people.sort()
        res = 0

        # [1,4,6,9] limit=10
        # remaining = limit - right = 10-9=1
        # if left == remaining, then res++, left += 1, right -= 1
        # if left > remaining, then res++, right -= 1
        # if left < remaining, left += 1

        while left <= right:
            remaining = limit - people[right]
            right -= 1
            res += 1
            if people[left] <= remaining:
                left += 1
            

            
        
        return res






            





        