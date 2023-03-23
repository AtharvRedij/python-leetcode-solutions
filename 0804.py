class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morse_reprs = set()
        for word in words:
            morse = "".join([morse_codes[ord(letter) - 97] for letter in word])
            morse_reprs.add(morse)

        return len(morse_reprs)
