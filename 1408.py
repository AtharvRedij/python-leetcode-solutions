class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for i, word in enumerate(words):
            for j, inner_word in enumerate(words):
                if i == j:
                    continue
                
                if word in inner_word:
                    result.append(word)
                    break

        return result
