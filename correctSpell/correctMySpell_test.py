"""Test Code for correctMySpell.py"""
from correctSpell.correctMySpell import get_all_fixed_words, edits1
from words_db import WordsDataBase

db = WordsDataBase("../small_txt_files")


def test_edits1():
    assert edits1("hell") == {'hellp', 'hwell', 'fell', 'yell', 'hoell', 'hebll', 'helle', 'hyll', 'heldl', 'heel',
                              'rell', 'hdll', 'rhell', 'hrell', 'fhell', 'hxll', 'herl', 'uell', 'hekl', 'hepll',
                              'helyl', 'helgl', 'helt', 'heoll', 'kell', 'aell', 'helj', 'ehll', 'lhell', 'hdell',
                              'sell', 'hqell', 'hfll', 'zell', 'thell', 'holl', 'hvell', 'mhell', 'helz', 'hegll',
                              'hmll', 'hull', 'helxl', 'hexl', 'heil', 'iell', 'help', 'hcll', 'hellb', 'heml', 'hiell',
                              'hesll', 'hellx', 'heqll', 'helc', 'huell', 'hevll', 'hezll', 'helg', 'hill', 'ihell',
                              'cell', 'mell', 'hwll', 'henl', 'hvll', 'hel', 'hmell', 'hall', 'ehell', 'ohell', 'helhl',
                              'hello', 'hecll', 'pell', 'hsell', 'hjell', 'hbll', 'well', 'helpl', 'heul', 'hzell',
                              'hbell', 'heell', 'helf', 'hetll', 'vhell', 'hqll', 'hellm', 'helq', 'ell', 'hesl',
                              'hele', 'heyll', 'hnll', 'hnell', 'hehl', 'hhell', 'hcell', 'hfell', 'helql', 'helwl',
                              'phell', 'helzl', 'hejll', 'heal', 'shell', 'helil', 'xell', 'hekll', 'heljl', 'nell',
                              'hgll', 'ahell', 'hehll', 'hewll', 'qell', 'lell', 'heall', 'heltl', 'hellh', 'henll',
                              'yhell', 'hewl', 'hellj', 'oell', 'dell', 'helo', 'helx', 'chell', 'jhell', 'hela',
                              'helv', 'hkell', 'helnl', 'hebl', 'hely', 'hexll', 'helrl', 'hells', 'hlel', 'hetl',
                              'hxell', 'heull', 'hellz', 'htll', 'hemll', 'helli', 'uhell', 'helkl', 'hellk', 'helvl',
                              'helu', 'heol', 'hevl', 'whell', 'hefl', 'htell', 'helal', 'helld', 'bhell', 'qhell',
                              'xhell', 'hedl', 'helb', 'heln', 'hsll', 'hll', 'helk', 'hecl', 'helsl', 'vell', 'haell',
                              'zhell', 'hkll', 'helln', 'hezl', 'hellq', 'hell', 'helfl', 'hpll', 'helul', 'hellg',
                              'heyl', 'helel', 'hellf', 'dhell', 'hefll', 'hellr', 'heql', 'hrll', 'hellc', 'helcl',
                              'khell', 'tell', 'hlll', 'hgell', 'hellt', 'hepl', 'hellv', 'gell', 'hegl', 'hedll',
                              'heill', 'hels', 'held', 'helm', 'hpell', 'helml', 'hyell', 'helly', 'helol', 'heli',
                              'hhll', 'jell', 'helh', 'hella', 'helr', 'eell', 'hjll', 'hejl', 'hellu', 'ghell',
                              'nhell', 'hlell', 'helbl', 'helw', 'hellw', 'herll', 'hzll', 'helll', 'bell'}


def test_get_all_fixed_words():
    result = get_all_fixed_words("hell", db)
    expected_correct_words = ['hello', 'hll', 'hill', 'bell', 'fell', 'shell', 'help', 'tell', 'sell', 'cell', 'held', 'well']
    expected_incorrect_words = set(edits1("hell")) - set(expected_correct_words)

    assert set(result) == set(expected_correct_words)
    assert not any(word in result for word in expected_incorrect_words)