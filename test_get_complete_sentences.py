from get_complete_sentences import get_completions_for_user_input
from words_db import WordsDataBase


def test_completions_for_user_input():
    words_db = WordsDataBase("small_txt_files")
    user_input = "Eliminating Left"
    completions = get_completions_for_user_input(words_db, user_input)

    expected_completions = [
        "Eliminating Left Recursion and Left Factoring CFGs ...........................................903",
        "Eliminating Left Recursion and Left Factoring CFGs",
        "“Eliminating Left Recursion and Left Factoring CFGs” on page 903. You",
        "eliminating left recursion. The",
        "“Eliminating Left Recursion and Left Factoring CFGs” on page 903",
        "Eliminating left recursion 903"
    ]

    assert completions == expected_completions

