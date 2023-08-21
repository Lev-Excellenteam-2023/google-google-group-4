import os
import re
from typing import List, Tuple, Union


class WordsDataBase:
    """
    Loading and managing word occurrences in the files.
    """
    WORDS_PATTERN = r"[^a-zA-Z1-9\s]"
    TXT_PREFIX = ".txt"
    SENTENCE_NUM_INDEX = 0
    WORD_NUM_INDEX = 1

    def __init__(self, root_path: str):
        """
        Initialize a WordsDataBase instance.
        :param root_path: The root directory path containing text files.
        """
        self.words_db = {}
        self.sentences = {}
        self.root_path = root_path
        self.lines_counter = 0
        self._load_words()

    def _tokenize_words(self, sentence: str) -> List[str]:
        """
        Tokenize a sentence into words.
        :param sentence: The sentence to tokenize
        :return: List[str]: List of words in the sentence
        """
        sentence = re.sub(self.WORDS_PATTERN, "", sentence)
        words = sentence.strip().lower().split()
        return words

    def _process_text_file(self, file_path: str):
        """
        Extracting word occurrences from a file for updating the word database.
        :param file_path: The path to the text file.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            for sentence in file:
                self.sentences[self.lines_counter] = sentence
                words = self._tokenize_words(sentence)
                for word_idx, word in enumerate(words):
                    if word in self.words_db:
                        self.words_db[word].append((self.lines_counter, word_idx))
                    else:
                        self.words_db[word] = [(self.lines_counter, word_idx)]
                self.lines_counter += 1

    def _load_words(self):
        """ Load the words to the DB"""
        for root, _, files in os.walk(self.root_path):
            for file_name in files:
                if file_name.endswith(self.TXT_PREFIX):
                    file_path = os.path.join(root, file_name)
                    self._process_text_file(file_path)

    def get_index(self, word: str, sentence_number: int) -> Union[int, None]:
        """
        Get the index of a word in a specific sentence.
        :param word: The word to look up.
        :param sentence_number: The sentence number to search within.
        :return: The index of the word in the sentence, or None if not found
        """
        word_indices = [indices for indices in self.words_db[word] if
                        indices[self.SENTENCE_NUM_INDEX] == sentence_number]
        if word_indices:
            return word_indices[0][self.WORD_NUM_INDEX]

    def get_all_positions(self, word: str) -> Union[List[Tuple[int, int]], None]:
        """
         Get all positions (sentence and word indices) of a word in the text.
        :param word: The word to look up.
        :return: List of all positions of the word in the text.
        """
        if word in self.words_db:
            return self.words_db[word]

    def get_full_sentence(self, sentence_number_and_offset: Tuple[int, int]) -> Union[List[Tuple[int, int]], None]:
        """
         Get all positions (sentence and word indices) of a word in the text.
        :param sentence_number_and_offset:
        :return: List of all positions of the word in the text.
        """
        if sentence_number_and_offset in self.words_db:
            return self.words_db[sentence_number_and_offset]

    def get_sentence(self, sentence_number: int) -> str:
        """
        Get a sentence by its number.
        :param sentence_number: The sentence number to get.
        :return: The sentence.
        """
        if sentence_number in self.sentences:
            return self.sentences[sentence_number]

    def get_sub_sentence(self, sentence_number: int, offset: int) -> str:
        """
        Get a sentence by its number.
        :param sentence_number: The sentence number to get.
        :param offset: The number of the word to start from.
        :return: The sub sentence from the offset.
        """
        sentence = self.get_sentence(sentence_number)
        sub_sentence = sentence.split()[offset:]
        return " ".join(sub_sentence)

    def get_complete_sentence(self, word_position_in_sentence_number: Tuple[int, int]) -> str:
        """
        Get a sentence by its number.
        :param word_position_in_sentence_number: Tuple of the sentence number and the word position in the sentence (offset).
        :return: The sub sentence from the offset to the end of the sentence.
        """
        sentence_number = word_position_in_sentence_number[0]
        offset = word_position_in_sentence_number[1]
        complete_sentence = self.get_sub_sentence(sentence_number, offset)
        return complete_sentence


# # init the database:
# words_db = WordsDataBase("small_txt_files")
#
# print(words_db.get_sentence(14))
# print(words_db.get_sub_sentence(14, 1))
# print(words_db.get_complete_sentence((14, 1)))
#
# user_input = "Eliminating Left"
# lower_user_input = user_input.lower()
# print(words_db.get_index("eliminating", 903))
# print("======================================================")
# user_input_words = words_db._tokenize_words(lower_user_input)
# for word in user_input_words:
#     print(words_db.get_all_positions(word))
