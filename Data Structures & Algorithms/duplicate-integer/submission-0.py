class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = False
        # 1. Instantiate dictionary to store each unique value and its count
        duplicate_dict = {}

        # 2. Let's loop through the nums list and add the key:value pairs to the dict
        for num in nums:
            if num not in duplicate_dict:
                duplicate_dict[num] = 1
            else:
                duplicate_dict[num] += 1
        
        # 3. We can then go through the duplicate_dict dictionary and check if any 'value' is > 1
        for key in duplicate_dict:
            if duplicate_dict[key] > 1:
                isDuplicate = True
            else:
                continue

        # 4. Return isDuplicate
        return isDuplicate
