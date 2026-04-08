class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ret_list = []
        left = 0
        right = len(numbers) - 1

        # [-5,-3,0,2,4,6,8] target = 5
        # [5,8,10,12,15,18] target = 20
        while left < right:
            comp_sum = numbers[left] + numbers[right]
            if comp_sum == target:
                ret_list = [left + 1, right + 1]
                break
            elif comp_sum > target:
                right -= 1
            elif comp_sum < target:
                left += 1
    
        return ret_list

        