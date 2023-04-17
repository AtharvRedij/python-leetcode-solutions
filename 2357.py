class Solution:
    def get_smallest_non_zero(self, arr):
        num = None
        for n in arr:
            if n != 0:
                if num is None:
                    num = n
                else:
                    num = min(num, n)

        return num

    def minimumOperations(self, nums: List[int]) -> int:
        result = 0 

        while True:
            subtracted = False
            smallest = self.get_smallest_non_zero(nums)
            if smallest is None:
                break

            for i in range(len(nums)):
                if nums[i]:
                    subtracted = True
                    nums[i] -= smallest

            if subtracted is False:
                break

            result += 1

        return result
