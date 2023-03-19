class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degrees = {}
        max_degree = None
        max_degree_nums = []

        for n in nums:
            if n in degrees:
                degrees[n] += 1
            else:
                degrees[n] = 1

            if max_degree is None or degrees[n] > max_degree:
                max_degree = degrees[n]
                max_degree_nums = [n]
            elif degrees[n] == max_degree:
                max_degree_nums.append(n)

        minimum_subarray_length = None
        for max_degree_num in max_degree_nums:
            degree = max_degree
            subarray = []
            for n in nums:
                if len(subarray) == 0 and n != max_degree_num:
                    continue

                subarray.append(n)

                if n == max_degree_num:
                    degree -= 1

                if degree <= 0:
                    break

            if minimum_subarray_length is None or len(subarray) < minimum_subarray_length:
                minimum_subarray_length = len(subarray)

        return minimum_subarray_length
