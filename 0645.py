class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        possible_nums = set(range(1, len(nums) + 1))
        repeating_num = None

        for n in nums:
            try:
                possible_nums.remove(n)
            except:
                repeating_num = n

        return repeating_num, possible_nums.pop()
      
