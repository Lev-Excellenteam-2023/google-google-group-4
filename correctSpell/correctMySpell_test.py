"""Test Code for correctMySpell.py"""

import unittest
from correctMySpell import words, P, correction, candidates, known, edits1

def test_words():
    assert words('This is a test.') == ['this', 'is', 'a', 'test']

def test_P():
    assert P('the') == 0.07240666483990596

def test_correction():
    assert correction('speling') == 'spelling'
    assert correction('korrected') == 'corrected'
    assert correction('bycycle') == 'bicycle'
    assert correction('inconvient') == 'inconvenient'
    assert correction('arrainged') == 'arranged'
    assert correction('peotry') == 'poetry'
    assert correction('peotryy') == 'poetry'
    assert correction('word') == 'word'

def test_candidates():


