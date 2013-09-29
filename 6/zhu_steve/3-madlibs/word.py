import re

VOWEL_PAT = re.compile('[aeiou]')
ADJACENT_VOWEL_PAT = re.compile('[aeiou]{2,}')

class Word:
    _word = ""

    def __init__(self, word):
        self._word = word

    def __str__(self):
        return self._word

    def plural(self):
        return self._word + 's'

    def gerund(self):
        w = self._word
        if w[-1] == 'e':
            w = w[:-1]
        # if does not end with vowel and there is only 1 vowel before the last letter
        elif not VOWEL_PAT.search(w[-1]) and not VOWEL_PAT.search(w[-3]):
            w += w[-1]
        return w + 'ing'

    def num_syllables(self):
        num_vowels = len(VOWEL_PAT.findall(self._word))
        num_adjacent = len(ADJACENT_VOWEL_PAT.findall(self._word))
        silent_e = 1 if self._word[-1] == 'e' else 0
        return num_vowels - num_adjacent - silent_e

if __name__ == "__main__":
    print Word("sit").gerund()
