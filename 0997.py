class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trust_counts = {}
        people_who_trust_others = set()

        for trust_from, trust_to in trust:
            people_who_trust_others.add(trust_from)
            trust_counts[trust_to] = trust_counts.get(trust_to, 0) + 1

        for person, trust_count in trust_counts.items():
            if trust_count == n-1 and person not in people_who_trust_others:
                return person
        

        return -1
