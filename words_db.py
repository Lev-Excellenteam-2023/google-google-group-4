import os
import re
from typing import List, Tuple, Union


class WordsDataBase:
    """
    Loading and managing word occurrences in the files.
    """
    WORDS_PATTERN = r"[^a-zA-Z\s]"
    TXT_PREFIX = ".txt"
    SENTENCE_NUM_INDEX = 0
    WORD_NUM_INDEX = 1

    def __init__(self, root_path: str):
        """
        Initialize a WordsDataBase instance.
        :param root_path: The root directory path containing text files.
        """
        self.words_db = {}
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
