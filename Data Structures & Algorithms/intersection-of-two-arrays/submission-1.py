class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        print(f'set1: {set1}')
        print(f'set2: {set2}')

        # Find intersection of both sets
        res = list(set1 & set2)

        # find union
        res_union = list(set1 | set2)
        print(f'res union: {res_union}')
        return res

        