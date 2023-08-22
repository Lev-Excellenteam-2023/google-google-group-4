"""Spelling Corrector in Python 3; see http://norvig.com/spell-correct.html

Copyright (c) 2007-2016 Peter Norvig
MIT license: www.opensource.org/licenses/mit-license.php
"""

import re
from collections import Counter
from words_db import WordsDataBase


# re.findall() returns a list of all the found matches, in the order they appeared in the string.
# \w+ matches any word character (equal to [a-zA-Z0-9_])
# + Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
# text.lower() returns a copy of the string in which all case-based characters have been lower cased.
def words(text): return re.findall(r'\w+', text.lower())


# Counter is a dict subclass for counting hashable objects.
# words(open('big.txt').read()) returns a list of all the words in the file big.txt
WORDS_DEC = Counter(words(open('..\\txt_files\\Concepts.txt', encoding='utf-8').read()))


def P(word, N=sum(WORDS_DEC.values())):
    """Probability of `word`."""
    return WORDS_DEC[word] / N  # N is the total number of words in the corpus


def correction(word):
    """Most probable spelling correction for word."""
    return max(candidates(word), key=P)


def candidates(word):
    """Generate possible spelling corrections for word."""
    return known([word]) or known(edits1(word)) or [word]  # known() returns a set of words from the list of words


def known(words):
    """The subset of `words` that appear in the dictionary of WORDS."""
    return set(w for w in words if w in WORDS_DEC)


def edits1(word):
    """All edits that are one edit away from `word`."""
    letters = 'abcdefghijklmnopqrstuvwxyz'

    # splits = [('','word'),('w','ord'),('wo','rd'),('wor','d'),('word','')]
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]

    # deletes = ['ord','wrd','wod','wor']
    deletes = [L + R[1:] for L, R in splits if R]

    # transposes = ['owrd','wrod','wodr']
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]

    # replaces = ['aord','bord','cord',...,'wora','worb','worc',...,'worda','wordb','wordc',...,'wordz']
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]

    # inserts = ['aword','bword','cword',...,'worda','wordb','wordc',...,'wordz']
    inserts = [L + c + R for L, R in splits for c in letters]

    return set(deletes + transposes + replaces + inserts)


def get_all_fixed_words(word: str, database: WordsDataBase) -> list[str]:
    """Returns a list of all the possible corrections for the given word"""
    all_words = edits1(word)
    fixed_words = [fixed_word for fixed_word in all_words if database.is_in_db(fixed_word)]
    wrong_words = [wrong_word for wrong_word in all_words if not database.is_in_db(wrong_word)]
    print(f"Wrong words: {wrong_words}")
    return fixed_words


db = WordsDataBase("../small_txt_files")
print(edits1("hell"))
# print(get_all_fixed_words("hell", db))
