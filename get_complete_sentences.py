import itertools
import re
from get_completions import get_all_sentences_number_that_contains_user_input
from AutoCompleteData import AutoCompleteData
from words_db import WordsDataBase
from correctSpell.correctMySpell import get_all_fixed_words


def get_completions_for_user_input(words_db: WordsDataBase, user_input: str) -> list[tuple[str, int]]:
    """
    @summary:
        Get all sentences that contains the user input.
    @param words_db: WordsDataBase
        The database of the words and sentences.
    @param user_input: str
        The user input.
    @return: list[tuple[str, int]]
        List of Tuples
        the first element is the complete sentence
        the second element is the sentence number
    """
    lower_user_input = user_input.lower()
    user_input_words = words_db._tokenize_words(lower_user_input)
    words_position_user_input = [words_db.get_all_positions(word) for word in user_input_words]
    sentences_number = get_all_sentences_number_that_contains_user_input(*words_position_user_input)
    sentences_number.sort(key=lambda tup: tup[0])
    sentence_numbers_to_loop = [number for number, _ in sentences_number]
    offsets = [offset for _, (offset, _) in sentences_number]
    tuple_sentences_offset = list(zip(sentence_numbers_to_loop, offsets))
    complete_sentences = [(words_db.get_complete_sentence(tuple_sentence_offset), sentence_number) for sentence_number, tuple_sentence_offset in zip(sentence_numbers_to_loop, tuple_sentences_offset)]
    return complete_sentences


def get_all_fixed_sentence(database: WordsDataBase, user_input: str) -> list[str]:
    """
    @summary:
        Get all sentences that derived from the user input by fixing the spelling mistakes if there are any.
    @param database: WordsDataBase
        The database of the words and sentences.
    @param user_input: str
        The user input.
    @return: list[str]
        List of all sentences that derived from the user input.
    @example:
        get_all_fixed_sentence(db, "W1, W2, W3")
        derived_W1 = ['W1A, W1B, W1C']
        derived_W2 = ['W2A, W2B, W2C']
        derived_W3 = ['W3A, W3B, W3C']

        derived_sentences = ["W1A W2A W3A", "W1A W2A W3B", "W1A W2A W3C", ... , "W1C W2C W3C"]
    """
    words_user_input = database.tokenize_words(user_input)
    fixed_words_user_input = [get_all_fixed_words(word, database) for word in words_user_input]

    # Generate all combinations of corrected words
    word_combinations = itertools.product(*fixed_words_user_input)
    all_derived_sentences = []
    for combo in word_combinations:
        derived_sentence = " ".join(combo)
        all_derived_sentences.append(derived_sentence)
    return all_derived_sentences


def get_completions_for_derived_user_input(database: WordsDataBase, user_input: str) -> list[tuple[str, int]]:
    """
    @summary:
        Get all sentences that derived from the user input by fixing the spelling mistakes if there are any.
        For each derived sentence, get all completions without duplicates.
    @param database: WordsDataBase
        The database of the words and sentences.
    @param user_input: str
        The user input.
    @return: list[tuple[str, int]]
        List of tuples, where each tuple contains the complete sentence and its sentence number.
    @example:
        get_completions_for_derived_user_input(db, "W1, W2, W3")
        derived_W1 = ['W1A, W1B, W1C']
        derived_W2 = ['W2A, W2B, W2C']
        derived_W3 = ['W3A, W3B, W3C']

        derived_sentences = ["W1A W2A W3A", "W1A W2A W3B", "W1A W2A W3C", ... , "W1C W2C W3C"]
        completions = [("Completion1", sentence_number1), ("Completion2", sentence_number2), ...]
    """
    derived_sentences = get_all_fixed_sentence(database, user_input)

    all_complete_sentences_set = set()  # Use a set to avoid duplicates

    for derived_sentence in derived_sentences:
        complete_sentences_tuple = get_completions_for_user_input(database, derived_sentence)
        complete_sentences = [(complete_sentence, sentence_number) for complete_sentence, sentence_number in complete_sentences_tuple]
        all_complete_sentences_set.update(complete_sentences)

    all_complete_sentences = list(all_complete_sentences_set)
    return all_complete_sentences


def get_decrease_grade(user_word: str, db_word: str) -> int:
    """
    @summary:
        Get the decrease grade of the user word compared to the database word.
    @param user_word: str
        The user word.
    @param db_word: str
        The database word.
    @return: int
        The decrease grade of the  database word compared to the user word.
    """
    user_word = re.sub(r'[^a-zA-Z0-9]', '', user_word)
    user_word = user_word.lower()
    db_word = re.sub(r'[^a-zA-Z0-9]', '', db_word)
    db_word = db_word.lower()
    if len(user_word) == len(db_word):
        if user_word == db_word:
            return 0
        for i in range(len(user_word)):
            if user_word[i] != db_word[i]:
                return min(-5 + i, -1)
    elif len(user_word) < len(db_word):
        for i in range(len(user_word)):
            if user_word[i] != db_word[i]:
                return min(-10 + 2 * i, -2)
        return max(10 - 2 * len(user_word), 0)
    else:  # len(user_word) > len(db_word)
        for i in range(len(db_word)):
            if user_word[i] != db_word[i]:
                return min(-10 + 2 * i, -2)
    return 0


def get_sentence_grade(user_input: str, db_sentence: str) -> int:
    """
    @summary:
        Get the grade of the user input compared to the sentence from the database.
    @param user_input: str
        The user input.
    @param db_sentence: str
        The sentence from the database.
    @return: int
        The grade of the sentence from the database compared to the user input.
    """
    user_words = user_input.split()
    db_words = db_sentence.split()
    db_words = db_words[:len(user_words)]
    # init grade = the number of user letters - not including spaces
    grade = 2 * (len(user_input) - user_input.count(" "))
    for i in range(min(len(user_words), len(db_words))):
        grade += get_decrease_grade(user_words[i], db_words[i])  # Add the increase in grade
    return max(grade, 0)


def get_best_k_completions(database: WordsDataBase, user_input: str, k: int) -> list[AutoCompleteData]:
    completions_tuple = get_completions_for_derived_user_input(database, user_input)
    sentence_numbers = [sentence_number for _, sentence_number in completions_tuple]
    completions = [sentence for sentence, _ in completions_tuple]
    grades = [get_sentence_grade(user_input, completion) for completion in completions]

    # Create AutoCompleteData objects and sort them by grade (score)
    auto_complete_data_list = [
        AutoCompleteData(completion, database.get_sentence(sentence_number), 0, sentence_number, grade)  # Switched offset and sentence_number
        for completion, sentence_number, grade in zip(completions, sentence_numbers, grades)
    ]
    auto_complete_data_list.sort(key=lambda data: data.score, reverse=True)

    return auto_complete_data_list[:k]


# db = WordsDataBase("small_txt_files")
# temp = get_completions_for_user_input(db, "hello world")
# temp = [sentence for sentence, _ in temp]
# print(temp)
# print(get_completions_for_derived_user_input(db, "hell"))
# # print(get_all_fixed_sentence(db, "hello world"))
# # print(get_completions_for_derived_user_input(db, "hello world"))
# # print(get_sentence_grade("hello world", "‘Hello world’. The algorithm for the delete"))
# AutoCompleteData = get_best_k_completions(db, "this", 5)
# for data in AutoCompleteData:
#     print(data.completed_sentence)
#     print(db.get_sentence(data.sentence_number))
#     print(data.score)

