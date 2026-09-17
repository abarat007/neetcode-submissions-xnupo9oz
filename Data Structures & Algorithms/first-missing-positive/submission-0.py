class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # we can make an array that stores 0 thru n+1
        n = len(nums)
        # res = [0] * n
        # print(res)

        # since we want the smallest positive value, ignore the negative values
        # nums = [-2,-1,0]
        # n = 3

        # we know that the answer has to liewithin the range (inclusive) 1 to n+1
        # nums = [1,2,4]
        # 1 : idx 0
        # 2 : idx 1
        # 3 : idx 2

        s = set(nums)
        x = 1
        while x in s:
            x += 1
        return x

        



        