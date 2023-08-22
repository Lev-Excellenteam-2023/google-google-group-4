import argparse
import time
from AutoCompleteData import AutoCompleteData

from get_complete_sentences import get_completions_for_user_input, get_best_k_completions
from words_db import WordsDataBase


def main():
    parser = argparse.ArgumentParser(description="CLI Demo for Getting Completions")
    parser.add_argument("root_path", type=str, help="Path to the root directory containing text files")

    args = parser.parse_args()
    k = 5
    print("Loading database...")
    words_db = WordsDataBase(args.root_path)
    print("Database loaded")
    time.sleep(1)
    print("\033[H\033[J")

    saved_prefix = ""

    while True:
        # Adjust the input prompt
        user_input = input(f"The system is ready. input: {saved_prefix}")
        if user_input == "#":
            saved_prefix = ""
            print("\033[H\033[J")
            continue
        else:
            saved_prefix += user_input
            current_input = saved_prefix

        try:
            completions = get_best_k_completions(words_db, current_input, k)
            if completions:
                print("Completions:")
                for idx, completion in enumerate(completions, start=1):
                    print(f"{idx}. {completion.completed_sentence} (score: {completion.score})")
            else:
                print("No completions")
        except Exception as e:
            print("No completions")

if __name__ == "__main__":
    main()




