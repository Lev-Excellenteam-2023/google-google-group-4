from typing import List, Tuple, Union, Any


def get_all_sentences_number(word_position_list: List[Tuple[int, int]]) -> Tuple[int]:
    """
    @summary:
        Get all sentences number that the word appears in all the DB.
    @param word_position_list: (List[Tuple[int, int]])
        List of tuples of word positions - all the positions that the word appears in all the DB.
        Each tuple contains 2 integers: (sentence number, word number in sentence).
    @return: (Tuple[int])
        Tuple of all sentences number from a word position list.
    @example:
       get_all_sentences_number([(1, 2), (3, 4), (5, 6), (7, 8)]) == (1, 3, 5, 7)
    """
    return tuple([word_position[0] for word_position in word_position_list if word_position is not None])


def intersection_of_sentences(*sentences_number_word_appear: Tuple[int]) -> tuple[Any, ...]:
    """
    @summary:
        Get all the sentences numbers that all the user's words appears in.
    @param sentences_number_word_appear: (Tuple[int])
        Unlimited number of tuples.
        Each tuple contains all the sentences number that a word in index i+1 appears in.
    @return: (Tuple[int])
        Tuple of all sentences number that all the user's words appears in.
    @example:
        index i=0: word1 appears in sentences 1,2,3,4,5
        index i=1: word2 appears in sentences 1,2,3,5
        index i=2: word3 appears in sentences 1,2,3,5,6
        intersection_of_sentences((1,2,3,4,5), (1,2,3,5), (1,2,3,5,6)) == (1,2,3,5)
    """
    # TODO: MAKE THE INTERSECTION LIKE TREE 1and2, 3and4 and then 1and2and3and4
    return tuple(set.intersection(*[set(sentences_number) for sentences_number in sentences_number_word_appear]))


def remove_nonexistent_sentences(positions_word: List[Tuple[int, int]], existed_sentences_number: int) -> List[
    Tuple[int, int]]:
    """
    @summary:
        Remove all the tuple of word positions that the sentence number
        is not in the existed_sentences_number(the numbers of sentences that all the user's words appears in).
    @param positions_word: (List[Tuple[int, int]])
        List of tuples of word positions - all the positions that the word appears in all the DB.
        Each tuple contains 2 integers: (sentence number, word number in sentence).
    @param existed_sentences_number: (Tuple[int])
        Tuple of all sentences number that all the user's words appears in.
    @return: (List[Tuple[int, int]])
        List of tuples of word positions - all the positions that the word appears in all the DB after
        removing tuples that the sentence number is not in
        the existed_sentences_number(the numbers of sentences that all the user's words appears in).
    """
    return [word_position for word_position in positions_word if word_position[0] in existed_sentences_number]


def get_word_positions_by_sentence_number(word_position_list: List[Tuple[int, int]], sentence_number: int) -> Tuple[int]:
    """
    @summary:
        Get list of tuples (the number of tuples is the number of the user words) of word positions in a specific sentence number.
    @param word_position_list: (List[Tuple[int, int]])
        List of tuples of word positions - Positions that the word appears in all the DB.
        Each tuple contains 2 integers: (sentence number, word number in sentence).
    @param sentence_number: (int)
        The number of a sentence.
    @return: (Tuple[int])
        List of tuples (the number of tuples is the number of the user words).
        Each tuple contains all the word positions in a specific sentence number.
    @example:
        index i=0: the word appears in sentences 1 at the 2nd word in the sentence.
        index i=1: the word appears in sentences 1 at the 4th word in the sentence.
        index i=2: the word appears in sentences 1 at the 6th word in the sentence.
        index i=3: the word appears in sentences 7 at the 8th word in the sentence.
        get_word_positions_by_sentence_number([(1, 2), (1, 4), (1, 6), (7, 8)], 1) == (2, 4, 6)
    """
    return tuple([word_position[1] for word_position in word_position_list if word_position[0] == sentence_number])


def increase_by_x(word_positions_in_sentence: Tuple[int], x: int) -> Tuple[int]:
    """
    @summary:
        Increase all the values in the tuple by x.
    @param word_positions_in_sentence: (Tuple[int])
        Tuple that represents all the positions of a specific user-input's word in a specific sentence.
    @param x: (int)
        The number to increase by. - X will be the number of the word in the user's input.
    @return: (Tuple[int])
        Tuple that represents all the positions of a specific user-input's word in a specific sentence after increasing by x.
    """
    return tuple([position + x for position in word_positions_in_sentence])


def get_positions_of_user_input_in_sentence(*positions_word_at_sentence: Tuple[int]) -> list[
    tuple[Union[int, Any], Any]]:
    """
    @summary:
        Get the position of the user's input in a specific sentence.
    @param positions_word_at_sentence: (Tuple[int])
        Tuple that represents all the positions of a specific user-input's word in a specific sentence.
    @return: (List[Tuple[int]])
        List of tuples. Each tuple contains two integers:
        (position of first word user input in a specific sentence, position last user input in a specific sentence).
    @example:
        get_position_of_user_input_in_sentence((1,2,3),(2,3,6,7),(3,4,7,8)) => [(1,3),(2,4)]
        explanation: the user input is 3 words that appear in the specific sentence two times:
        1st: from the 1st word to the 3rd word in the sentence.
        2nd: from the 2nd word to the 4th word in the sentence.
    """
    user_input_len = len(positions_word_at_sentence)
    positions_word_at_sentence = [increase_by_x(positions_word_at_sentence[i], user_input_len - i - 1) for i in
                                  range(user_input_len)]

    intersection_positions_word_at_sentence = set.intersection(
        *[set(positions_word) for positions_word in positions_word_at_sentence])

    first_to_end_positions_of_user_input_in_sentence = [(position - user_input_len + 1, position) for
                                                        position in intersection_positions_word_at_sentence]
    return first_to_end_positions_of_user_input_in_sentence


def get_all_sentences_number_that_contains_user_input(*words_positions_list: Union[List[Tuple[int, int]]]) -> List[Tuple[int, Tuple[int]]]:
    """
    @summary:
        Get all the sentences number that contains the user's input and the offset of the user's input in the sentence.
    @param words_positions_list: (List[Tuple[int, int]])
        Unlimited (number of words of the user's input) of List of tuples of word positions - Positions that the word appears in all the DB.
        Each tuple contains 2 integers: (sentence number, word number in sentence).
    @return: (List[Tuple[int, Tuple[int]]])
        List of tuples that represent only the sentences number that contains the
        user's input and tuple of the offset of (the 1st word,the last word) user's input in the sentence.
    """
    # Remove None values from the input list
    filtered_words_positions_list = [positions for positions in words_positions_list if positions is not None]

    # step 1: foreach argument, get all the sentences number that contains the word:
    sentences_number = [get_all_sentences_number(word_positions) for word_positions in filtered_words_positions_list]

    # step 2: get the intersection of all the sentences number that contains the user's input:
    sentence_numbers_contains_all_user_input_words = intersection_of_sentences(*sentences_number)

    # step 3: remove from the words_positions_list all the tuples that
    # the sentence number is not in sentence_numbers_contains_all_user_input_words -  using remove_nonexistent_sentences function:
    filtered_words_positions = [
        remove_nonexistent_sentences(word_positions, sentence_numbers_contains_all_user_input_words)
        for word_positions in filtered_words_positions_list
    ]

    # step 4: foreach sentence in sentence_numbers_contains_all_user_input_words (is:(1,3,7)), append
    sentences = []
    for number_of_sentence in sentence_numbers_contains_all_user_input_words:
        words_positions_in_sentence = []
        for word_positions in filtered_words_positions:
            words_positions_in_sentence.append(get_word_positions_by_sentence_number(word_positions, number_of_sentence))
        sentences.append(words_positions_in_sentence)

    # step 5: foreach sentence in sentences apply get_positions_of_user_input_in_sentence function:
    sentences = [get_positions_of_user_input_in_sentence(*sentence) for sentence in sentences]

    # step 6: Union of the tuples of the word positions for the sentence in which they are contained
    contains_sentences_numbers = []
    for sentence_number, sentence in zip(sentence_numbers_contains_all_user_input_words, sentences):
        for position in sentence:
            contains_sentences_numbers.append((sentence_number, position))
    # print(contains_sentences_numbers)
    return contains_sentences_numbers

# TODO: integrate the last method with the new DB to return the actual sentences
#       and the complete user input to return at the end of the AutoCompleteData Object.
