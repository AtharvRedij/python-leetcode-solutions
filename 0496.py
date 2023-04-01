class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_element_map = {}
        stack = []

        for n in nums2:
            while stack and n > stack[-1]:
                next_greater_element_map[stack[-1]] = n
                stack.pop(-1)

            stack.append(n)

        for n in stack:
            next_greater_element_map[n] = -1

        return [next_greater_element_map[n] for n in nums1] 
