class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_no_of_words = 0
        for sentence in sentences:
            max_no_of_words = max(max_no_of_words, sentence.count(" ") + 1)
        return max_no_of_words
