class Solution:
    def get_gcd(self, x, y):
        if x < y:
            return self.get_gcd(y, x)
        elif x % y == 0:
            return y
        else:
            return self.get_gcd(x-y, y)

    def findGCD(self, nums: List[int]) -> int:
        return self.get_gcd(max(nums), min(nums))
