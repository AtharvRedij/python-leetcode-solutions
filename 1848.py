class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_value = None

        for i in range(len(nums)):
            if nums[i] == target:
                if min_value is None:
                    min_value = abs(i-start)
                else:
                    min_value = min(min_value, abs(i-start))

        return min_value
