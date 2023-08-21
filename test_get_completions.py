from get_completions import (
    get_all_sentences_number,
    intersection_of_sentences,
    remove_nonexistent_sentences,
    get_word_positions_by_sentence_number,
    increase_by_x,
    get_positions_of_user_input_in_sentence,
    get_all_sentences_number_that_contains_user_input
)


# Test for get_all_sentences_number
def test_get_all_sentences_number():
    assert get_all_sentences_number([(1, 2), (3, 4), (5, 6), (7, 8)]) == (1, 3, 5, 7)


# Test for intersection_of_sentences
def test_intersection_of_sentences():
    assert intersection_of_sentences((1, 2, 3, 4, 5), (1, 2, 3, 5), (1, 2, 3, 5, 6)) == (1, 2, 3, 5)


# Test for remove_nonexistent_sentences
def test_remove_nonexistent_sentences():
    assert remove_nonexistent_sentences([(1, 2), (3, 4), (5, 6), (7, 8)], (1, 3, 5)) == [(1, 2), (3, 4), (5, 6)]


# Test for get_word_positions_by_sentence_number
def test_get_word_positions_by_sentence_number():
    assert get_word_positions_by_sentence_number([(1, 2), (1, 4), (1, 6), (7, 8)], 1) == (2, 4, 6)


# Test for increase_by_x
def test_increase_by_x():
    assert increase_by_x((2, 4, 6), 2) == (4, 6, 8)


# Test for get_positions_of_user_input_in_sentence
def test_get_positions_of_user_input_in_sentence():
    assert get_positions_of_user_input_in_sentence((1, 2, 3), (2, 3, 6, 7), (3, 4, 7, 8)) == [(1, 3), (2, 4)]


# Test for get_all_sentences_number_that_contains_user_input
def test_get_all_sentences_number_that_contains_user_input():
    assert get_all_sentences_number_that_contains_user_input([(1, 2), (3, 4), (5, 6), (7, 8)], (1, 3, 5)) == (1, 3, 5)


# Test for get_all_sentences_number_that_contains_user_input
def test_get_all_sentences_number_that_contains_user_input():
    word1 = [(1, 1), (1, 2), (1, 3), (2, 11), (2, 12), (2, 13)]
    word2 = [(1, 2), (1, 3), (1, 6), (1, 7), (2, 2), (2, 3), (2, 6), (2, 7)]
    word3 = [(1, 3), (1, 4), (1, 7), (1, 8), (2, 3), (2, 4), (2, 7), (2, 8)]

    assert get_all_sentences_number_that_contains_user_input(word1, word2, word3) == [(1, (1, 3)), (1, (2, 4))]





