class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_counts = {}
        for num in target:
            target_counts[num]= target_counts.get(num, 0) + 1
        
        for num in arr:
            if num not in target_counts:
                return False
            elif target_counts[num] == 0:
                return False
            else:
                target_counts[num] -= 1

        return True
