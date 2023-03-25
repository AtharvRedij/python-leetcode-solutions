class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        results = None

        for arr in nums:
            if results is None:
                results = set(arr)
            else:
                results = results.intersection(set(arr))


        return sorted(results)
