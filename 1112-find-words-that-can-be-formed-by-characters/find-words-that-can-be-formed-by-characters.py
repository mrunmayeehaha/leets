from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total = 0

        for w in words:
            words_count = Counter(w)

            if all(words_count[c] <= chars_count[c] for c in words_count):
                total = total + len(w)
        return total