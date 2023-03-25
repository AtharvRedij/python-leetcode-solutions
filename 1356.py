class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        numbers_with_same_one_count = {}

        for n in arr:
            one_count = "{0:b}".format(n).count('1')

            if one_count in numbers_with_same_one_count:
                numbers_with_same_one_count[one_count].append(n)
            else:
                numbers_with_same_one_count[one_count] = [n]

        possible_one_counts = sorted(numbers_with_same_one_count.keys())
        results = []
        for one_count in possible_one_counts:
            results.extend(sorted(numbers_with_same_one_count[one_count]))

        return results
