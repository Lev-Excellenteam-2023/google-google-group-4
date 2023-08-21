from get_completions import get_all_sentences_number_that_contains_user_input
from AutoCompleteData import AutoCompleteData
from words_db import WordsDataBase


def get_completions_for_user_input(words_db, user_input):
    lower_user_input = user_input.lower()
    user_input_words = words_db._tokenize_words(lower_user_input)
    words_position_user_input = [words_db.get_all_positions(word) for word in user_input_words]
    sentences_number = get_all_sentences_number_that_contains_user_input(*words_position_user_input)
    sentences_number.sort(key=lambda tup: tup[0])
    sentence_numbers_to_loop = [number for number, _ in sentences_number]
    offsets = [offset for _, (offset, _) in sentences_number]
    tuple_sentences_offset = list(zip(sentence_numbers_to_loop, offsets))
    complete_sentences = [words_db.get_complete_sentence(tuple_sentence_offset) for tuple_sentence_offset in tuple_sentences_offset]
    return complete_sentences


# Usage
words_db = WordsDataBase("small_txt_files")
user_input = "Eliminating Left"
completions = get_completions_for_user_input(words_db, user_input)
for completion in completions:
    print(completion)
