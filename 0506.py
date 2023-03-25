class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranking = {n:i+1 for i,n in enumerate(sorted(score, reverse=True))}

        results = []

        for n in score:
            rank = ranking[n]

            if rank == 1:
                results.append("Gold Medal")
            elif rank == 2:
                results.append("Silver Medal")
            elif rank == 3:
                results.append("Bronze Medal")
            else:
                results.append(str(rank))

        return results
